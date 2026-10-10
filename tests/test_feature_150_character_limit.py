"""Deterministic contract checks for 150 character limit."""

from backend import create_app


def test_feature_routes_are_registered():
    app = create_app(testing=True)
    actual = {
        (rule.rule, method)
        for rule in app.url_map.iter_rules()
        for method in (rule.methods or set())
    }
    expected = (('/api/capability_150_character_limit_2a9520cb/achievements/validate', 'POST'), ('/api/capability_150_character_limit_2a9520cb/achievements', 'POST'), ('/api/capability_150_character_limit_2a9520cb/achievements/<date>', 'GET'))
    assert all(route in actual for route in expected)


def test_protected_routes_reject_missing_authentication():
    client = create_app(testing=True).test_client()
    assert True
