"""Application factory retaining the generated feature/core layout."""
import os
from importlib import import_module
from pathlib import Path

from flask import Flask, jsonify
from sqlalchemy import text
from werkzeug.middleware.proxy_fix import ProxyFix

from backend.core.auth import install_auth
from backend.core.config import get_settings
from backend.core.db import configure_database, get_engine
from backend.core.errors import register_error_handlers


def create_app(testing=False, config=None):
    settings = get_settings(testing=testing)
    frontend = Path(__file__).resolve().parents[1] / "frontend"
    app = Flask(__name__, template_folder=str(frontend), static_folder=None)
    app.config.update(
        TESTING=bool(testing), DATABASE_URL=settings.database_url,
        JWT_SECRET=settings.jwt_secret, JWT_ISSUER=settings.jwt_issuer,
        SECRET_KEY=settings.jwt_secret, SESSION_COOKIE_NAME="daily_win_session",
        SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=os.getenv("COOKIE_SECURE", "false").lower() == "true",
        MAX_CONTENT_LENGTH=16 * 1024,
    )
    if config:
        app.config.update(config)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1)
    configure_database(app)
    register_error_handlers(app)
    install_auth(app)
    for feature in (
        "authentication", "local_browser_storage", "device_timezone_detection",
        "record_daily_achievement", "one_entry_per_day_limit", "150_character_limit",
        "duplicate_entry_prevention", "brief_microcopy",
    ):
        # import_module supports the original generated directory beginning with a digit.
        module = import_module(f"backend.features.{feature}.feature")
        app.register_blueprint(module.blueprint)

    @app.get("/health")
    def health():
        try:
            with get_engine().connect() as connection:
                connection.execute(text("SELECT 1"))
        except Exception:
            app.logger.exception("Database health check failed")
            return jsonify(ok=False, service="daily-win-backend", database="unavailable"), 503
        return jsonify(ok=True, service="daily-win-backend", database="ok")

    @app.after_request
    def response_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "same-origin"
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data:; connect-src 'self'; form-action 'self'; "
            "base-uri 'self'; frame-ancestors 'none'"
        )
        if response.mimetype in {"text/html", "application/json"}:
            response.headers["Cache-Control"] = "no-store"
        return response
    return app
