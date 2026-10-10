"""Whole-application smoke tests."""

from backend import create_app


def test_health_endpoint():
    app = create_app(testing=True)
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json()["ok"] is True


def test_expected_function_inventory_is_frozen():
    expected = ('capability_local_browser_storage_99d93461.function.save_win', 'capability_local_browser_storage_99d93461.function.get_wins', 'capability_local_browser_storage_99d93461.function.check_win_exists_for_date', 'capability_device_timezone_detection_aca07cc7.function.get_current_local_date', 'capability_device_timezone_detection_aca07cc7.function.check_entry_exists_for_date', 'capability_device_timezone_detection_aca07cc7.function.record_entry_local_date', 'capability_record_daily_achievement_86a57805.function.check_today_entry', 'capability_record_daily_achievement_86a57805.function.save_achievement', 'capability_one_entry_per_day_limit_86f08838.function.check_entry_exists_for_date', 'capability_one_entry_per_day_limit_86f08838.function.create_daily_win_entry', 'capability_one_entry_per_day_limit_86f08838.function.get_entry_for_date', 'capability_150_character_limit_2a9520cb.function.validate_achievement_text', 'capability_150_character_limit_2a9520cb.function.create_achievement', 'capability_150_character_limit_2a9520cb.function.get_achievement_by_date', 'capability_duplicate_entry_prevention_00baa1bc.function.check_today_win_exists', 'capability_duplicate_entry_prevention_00baa1bc.function.create_win_with_duplicate_check', 'capability_brief_microcopy_76537cc2.function.get_microcopy_strings', 'capability_brief_microcopy_76537cc2.function.initialize_microcopy_strings')
    assert len(expected) == 18
