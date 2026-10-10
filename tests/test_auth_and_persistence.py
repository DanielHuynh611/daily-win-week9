"""Behavior checks for real authentication, isolated ownership and durable wins."""
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import re

import pytest
from sqlalchemy import select

from fullstack import create_app
from backend.core.auth import AUTH_COOKIE, issue_token
from backend.core.db import users, wins

API = "/api/capability_local_browser_storage_99d93461/wins"


@pytest.fixture
def app():
    application = create_app(testing=True)
    yield application
    application.extensions["database_engine"].dispose()


def csrf(client, page="/"):
    response = client.get(page)
    return re.search(r'<meta name="csrf-token" content="([^"]+)"', response.text)[1]


def register(client, email="student@example.com", password="present123", confirmation=None):
    token = csrf(client, "/register")
    return client.post("/register", data={
        "email": email, "password": password,
        "confirm_password": password if confirmation is None else confirmation,
        "csrf_token": token,
    })


def headers(client, zone="UTC"):
    return {"X-CSRF-Token": csrf(client), "X-Time-Zone": zone}


def save(client, text="Finished a practice question", day=None, zone="UTC"):
    return client.post(API, json={
        "achievement_text": text, "date": day or datetime.now(ZoneInfo(zone)).date().isoformat(),
    }, headers=headers(client, zone))


def test_registration_opens_minimal_today_screen_and_hashes_password(app):
    client = app.test_client()
    assert register(client).status_code == 303
    response = client.get("/")
    assert response.status_code == 200
    assert "Today's win" in response.text
    assert '<span>Today</span>' in response.text
    assert 'id="win-form"' in response.text
    assert "Apply filters" not in response.text
    assert 'type="date"' not in response.text
    assert "Timezone Detection Service" not in response.text
    assert "--z-accent:#ff642f" in response.text
    assert 'class="z-sidebar"' in response.text
    assert "student@example.com" in response.text
    with app.extensions["database_engine"].connect() as connection:
        user = connection.execute(select(users)).mappings().one()
    assert user["password_hash"].startswith("pbkdf2_sha256$")
    assert user["password_hash"] != "present123"


@pytest.mark.parametrize("email,password,confirmation", [
    ("invalid-email", "present123", "present123"),
    ("student@example.com", "short", "short"),
    ("student@example.com", "present123", "different123"),
])
def test_registration_validation(app, email, password, confirmation):
    client = app.test_client()
    response = register(client, email, password, confirmation)
    assert response.status_code == 400
    assert 'role="alert"' in response.text
    assert client.get("/").status_code == 302


def test_duplicate_email_is_case_insensitive(app):
    assert register(app.test_client()).status_code == 303
    response = register(app.test_client(), "STUDENT@example.com")
    assert response.status_code == 409
    assert "already registered" in response.text


def test_login_logout_and_invalid_credentials(app):
    client = app.test_client()
    register(client)
    assert client.post("/logout", data={"csrf_token": csrf(client)}).status_code == 303
    assert client.get("/").headers["Location"] == "/login"
    assert client.get(API).status_code == 401
    token = csrf(client, "/login")
    bad = client.post("/login", data={
        "email": "student@example.com", "password": "incorrect123", "csrf_token": token,
    })
    assert bad.status_code == 401
    good = client.post("/login", data={
        "email": "student@example.com", "password": "present123", "csrf_token": token,
    })
    assert good.status_code == 303
    assert client.get("/").status_code == 200


def test_saved_win_visible_after_refresh_and_duplicate_blocked(app):
    client = app.test_client()
    register(client)
    result = save(client)
    assert result.status_code == 201
    win = result.get_json()
    assert client.get(API).get_json()["wins"] == [win]
    assert client.get(API + "/check?date=" + win["date"]).get_json()["exists"] is True
    assert save(client, "Another win").status_code == 409
    assert len(client.get(API).get_json()["wins"]) == 1


def test_accounts_can_record_same_day_without_reading_each_other(app):
    alice, bob = app.test_client(), app.test_client()
    register(alice, "alice@example.com")
    register(bob, "bob@example.com")
    assert save(alice, "Alice's private win").status_code == 201
    assert bob.get(API).get_json()["wins"] == []
    assert save(bob, "Bob's private win").status_code == 201
    assert alice.get(API).get_json()["wins"][0]["achievement_text"] == "Alice's private win"
    assert bob.get(API).get_json()["wins"][0]["achievement_text"] == "Bob's private win"


@pytest.mark.parametrize("text", ["", "   ", "x" * 151, None, 123, ["win"]])
def test_invalid_win_cannot_be_saved(app, text):
    client = app.test_client()
    register(client)
    assert save(client, text).status_code == 400
    assert client.get(API).get_json()["wins"] == []


def test_150_characters_accepted(app):
    client = app.test_client()
    register(client)
    assert save(client, "x" * 150).status_code == 201
    assert len(client.get(API).get_json()["wins"][0]["achievement_text"]) == 150


def test_only_current_local_date_allowed(app):
    client = app.test_client()
    register(client)
    today = datetime.now(ZoneInfo("UTC")).date()
    assert save(client, day=(today - timedelta(days=1)).isoformat()).status_code == 400
    assert save(client, day="2026-02-30").status_code == 400
    assert save(client, day=today.isoformat(), zone="Not/AZone").status_code == 400
    sydney_today = datetime.now(ZoneInfo("Australia/Sydney")).date().isoformat()
    assert save(client, day=sydney_today, zone="Australia/Sydney").status_code == 201


def test_all_generated_save_routes_share_duplicate_constraint(app):
    client = app.test_client()
    register(client)
    assert save(client).status_code == 201
    routes = [
        "/api/capability_record_daily_achievement_86a57805/achievements",
        "/api/capability_one_entry_per_day_limit_86f08838/daily-wins",
        "/api/capability_duplicate_entry_prevention_00baa1bc/wins",
        "/api/capability_150_character_limit_2a9520cb/achievements",
    ]
    for route in routes:
        response = client.post(route, json={
            "achievement_text": "Duplicate", "date": datetime.now(ZoneInfo("UTC")).date().isoformat(),
        }, headers=headers(client))
        assert response.status_code == 409


def test_csrf_required_for_browser_writes_and_auth(app):
    client = app.test_client()
    assert client.post("/register", data={"email": "a@example.com", "password": "present123"}).status_code == 400
    register(client)
    assert client.post(API, json={"achievement_text": "Test"}).status_code == 400
    assert client.post("/logout").status_code == 400


def test_unauthenticated_and_bad_tokens_are_rejected(app):
    client = app.test_client()
    assert client.get(API).status_code == 401
    assert client.post(API, json={"achievement_text": "Test"}).status_code == 401
    client.set_cookie(AUTH_COOKIE, "invalid.token.signature")
    assert client.get(API).status_code == 401
    assert client.get("/").status_code == 302


def test_expired_and_unknown_user_tokens_are_rejected(app):
    client = app.test_client()
    register(client)
    with app.app_context():
        with app.extensions["database_engine"].connect() as connection:
            user_id = connection.execute(select(users.c.id)).scalar_one()
        expired = issue_token(user_id, expires_in_seconds=-1)
        unknown = issue_token("missing-user")
    for token in (expired, unknown):
        client.set_cookie(AUTH_COOKIE, token)
        assert client.get(API).status_code == 401


def test_bearer_api_authentication_uses_the_same_owned_store(app):
    client = app.test_client()
    register(client)
    with app.app_context():
        with app.extensions["database_engine"].connect() as connection:
            user_id = connection.execute(select(users.c.id)).scalar_one()
        token = issue_token(user_id)
    external = app.test_client()
    response = external.post(API, json={"achievement_text": "Saved via API"},
                             headers={"Authorization": "Bearer " + token})
    assert response.status_code == 201
    assert client.get(API).get_json()["wins"][0]["achievement_text"] == "Saved via API"


def test_persistence_across_application_restart(tmp_path):
    config = {"DATABASE_URL": "sqlite+pysqlite:///" + str(tmp_path / "persistent.db")}
    first = create_app(testing=True, config=config)
    client = first.test_client()
    register(client)
    assert save(client, "Survives a restart").status_code == 201
    first.extensions["database_engine"].dispose()
    second = create_app(testing=True, config=config)
    client = second.test_client()
    token = csrf(client, "/login")
    assert client.post("/login", data={
        "email": "student@example.com", "password": "present123", "csrf_token": token,
    }).status_code == 303
    assert client.get(API).get_json()["wins"][0]["achievement_text"] == "Survives a restart"
    second.extensions["database_engine"].dispose()


def test_assets_and_legacy_screen_redirects(app):
    client = app.test_client()
    register(client)
    for route in ("/confirmation", "/internal/timezone-detection"):
        response = client.get(route)
        assert response.status_code == 302
        assert response.headers["Location"] == "/"
        response = client.get(route, follow_redirects=True)
        assert response.status_code == 200
        assert 'class="z-sidebar"' in response.text
        assert "--z-accent:#ff642f" in response.text
    for route in (
        "/static/css/app.css",
        "/__frontend_assets/frontend/shared/ui/library.js",
        "/__frontend_assets/frontend/shared/ui/runtime.js",
        "/__frontend_assets/frontend/features/local_browser_storage/daily_win.js",
        "/__frontend_assets/frontend/features/local_browser_storage/today.js",
    ):
        assert client.get(route).status_code == 200
    assert client.get("/__frontend_assets/frontend/core/config.py").status_code == 404


def test_auth_navigation_does_not_offer_signed_in_workflows(app):
    client = app.test_client()
    page = client.get("/login").text
    assert '<span>Today</span>' not in page
    assert '<nav' not in page
    assert 'class="z-sidebar"' not in page
    assert 'class="daily-auth"' in page
    assert 'href="/register"' in page
    assert "Main Win Entry Screen" not in page


def test_history_requires_login_and_has_active_navigation(app):
    client = app.test_client()
    assert client.get("/history").headers["Location"] == "/login"
    register(client)
    response = client.get("/history")
    assert response.status_code == 200
    assert 'href="/history" aria-current="page"' in response.text
    assert 'href="/" aria-current="page"' not in response.text
    assert 'id="history-empty"' in response.text
    assert 'id="history-list"' in response.text
    assert client.get('/__frontend_assets/frontend/features/local_browser_storage/history.js').status_code == 200


def test_both_auth_pages_have_no_navigation(app):
    client = app.test_client()
    for route in ("/login", "/register"):
        page = client.get(route).text
        assert '<nav' not in page
        assert '<aside' not in page
        assert 'data-nav-toggle' not in page
        assert 'id="main-content"' in page
        assert 'name="csrf_token"' in page


def test_secure_cookies_for_https_deployment():
    application = create_app(testing=True, config={"SESSION_COOKIE_SECURE": True})
    client = application.test_client()
    response = register(client)
    cookies = response.headers.getlist("Set-Cookie")
    assert any(cookie.startswith(AUTH_COOKIE + "=") and "HttpOnly" in cookie and "Secure" in cookie for cookie in cookies)
    assert all("SameSite=Lax" in cookie for cookie in cookies)
    application.extensions["database_engine"].dispose()
