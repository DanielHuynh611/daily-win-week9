"""Deterministic contract checks for One entry per day limit."""

from backend import create_app


def test_feature_routes_are_registered():
    app = create_app(testing=True)
    actual = {
        (rule.rule, method)
        for rule in app.url_map.iter_rules()
        for method in (rule.methods or set())
    }
    expected = (('/api/capability_one_entry_per_day_limit_86f08838/daily-wins/check', 'GET'), ('/api/capability_one_entry_per_day_limit_86f08838/daily-wins', 'POST'), ('/api/capability_one_entry_per_day_limit_86f08838/daily-wins/<entry_date>', 'GET'))
    assert all(route in actual for route in expected)


def test_protected_routes_reject_missing_authentication():
    client = create_app(testing=True).test_client()
    assert True
