# Architecture verification

These are contract and coverage checks, not executable application tests. Non-blocking findings describe issues intentionally retained in the generated files for you to inspect and repair. They do not mean the package is missing. Historical attempts may refer to an earlier scope; compare scope hashes.

## Findings and next steps

```json
{
  "finding": "cross_feature_table_concept_overlap",
  "code": "cross_feature_table_concept_overlap",
  "severity": "error",
  "blocking": false,
  "category": "database",
  "message": "Multiple features define separate tables for the same likely 'achievement' concept.",
  "affected_feature_ids": [
    "capability_150_character_limit_2a9520cb",
    "capability_record_daily_achievement_86a57805"
  ],
  "components": [
    {
      "feature_id": "capability_150_character_limit_2a9520cb",
      "component_id": "capability_150_character_limit_2a9520cb.table.achievements",
      "name": "f_2a9520cb__achievements"
    },
    {
      "feature_id": "capability_record_daily_achievement_86a57805",
      "component_id": "capability_record_daily_achievement_86a57805.table.achievements",
      "name": "f_86a57805__achievements"
    }
  ],
  "repair": "Inspect whether these tables represent one shared entity. If they do, keep one canonical table and update the affected feature queries and relationships."
}
```

Multiple features define separate tables for the same likely 'achievement' concept. Inspect whether these tables represent one shared entity. If they do, keep one canonical table and update the affected feature queries and relationships.

```json
{
  "finding": "cross_feature_screen_route_collision",
  "code": "cross_feature_screen_route_collision",
  "severity": "error",
  "blocking": false,
  "category": "frontend",
  "message": "Multiple features define screens for the same route '/'.",
  "affected_feature_ids": [
    "capability_150_character_limit_2a9520cb",
    "capability_brief_microcopy_76537cc2",
    "capability_confirmation_message_23ce028f",
    "capability_current_date_display_67c458ab",
    "capability_duplicate_entry_prevention_00baa1bc",
    "capability_local_browser_storage_99d93461",
    "capability_non_empty_validation_c7515c58",
    "capability_one_entry_per_day_limit_86f08838",
    "capability_record_daily_achievement_86a57805",
    "capability_save_button_5553765f",
    "capability_single_screen_interface_20b1b421"
  ],
  "components": [
    {
      "feature_id": "capability_150_character_limit_2a9520cb",
      "component_id": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
      "name": "Achievement Entry Screen",
      "route": "/"
    },
    {
      "feature_id": "capability_brief_microcopy_76537cc2",
      "component_id": "capability_brief_microcopy_76537cc2.screen.microcopy_display",
      "name": "Microcopy Display Screen",
      "route": "/"
    },
    {
      "feature_id": "capability_confirmation_message_23ce028f",
      "component_id": "capability_confirmation_message_23ce028f.screen.main_with_confirmation",
      "name": "Main Screen with Confirmation Message",
      "route": "/"
    },
    {
      "feature_id": "capability_current_date_display_67c458ab",
      "component_id": "capability_current_date_display_67c458ab.screen.main_entry",
      "name": "Main Entry Screen",
      "route": "/"
    },
    {
      "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
      "component_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
      "name": "Main Entry Screen",
      "route": "/"
    },
    {
      "feature_id": "capability_local_browser_storage_99d93461",
      "component_id": "capability_local_browser_storage_99d93461.screen.main",
      "name": "Main Win Entry Screen",
      "route": "/"
    },
    {
      "feature_id": "capability_non_empty_validation_c7515c58",
      "component_id": "capability_non_empty_validation_c7515c58.screen.main_entry",
      "name": "Main Entry Screen with Validation",
      "route": "/"
    },
    {
      "feature_id": "capability_one_entry_per_day_limit_86f08838",
      "component_id": "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry",
      "name": "Daily Win Entry Screen",
      "route": "/"
    },
    {
      "feature_id": "capability_record_daily_achievement_86a57805",
      "component_id": "capability_record_daily_achievement_86a57805.screen.main",
      "name": "Daily Achievement Entry",
      "route": "/"
    },
    {
      "feature_id": "capability_save_button_5553765f",
      "component_id": "capability_save_button_5553765f.screen.main_entry",
      "name": "Main Entry Screen",
      "route": "/"
    },
    {
      "feature_id": "capability_single_screen_interface_20b1b421",
      "component_id": "capability_single_screen_interface_20b1b421.screen.main",
      "name": "Main Recording Screen",
      "route": "/"
    }
  ],
  "repair": "Decide whether these responsibilities belong on one shared screen. Merge the screen behavior or assign distinct routes, then update navigation and actions."
}
```

Multiple features define screens for the same route '/'. Decide whether these responsibilities belong on one shared screen. Merge the screen behavior or assign distinct routes, then update navigation and actions.

```json
{
  "finding": "cross_feature_screen_concept_overlap",
  "code": "cross_feature_screen_concept_overlap",
  "severity": "error",
  "blocking": false,
  "category": "frontend",
  "message": "Multiple features define separate screens for the same likely 'main entry' responsibility.",
  "affected_feature_ids": [
    "capability_current_date_display_67c458ab",
    "capability_duplicate_entry_prevention_00baa1bc",
    "capability_save_button_5553765f"
  ],
  "components": [
    {
      "feature_id": "capability_current_date_display_67c458ab",
      "component_id": "capability_current_date_display_67c458ab.screen.main_entry",
      "name": "Main Entry Screen",
      "route": "/"
    },
    {
      "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
      "component_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
      "name": "Main Entry Screen",
      "route": "/"
    },
    {
      "feature_id": "capability_save_button_5553765f",
      "component_id": "capability_save_button_5553765f.screen.main_entry",
      "name": "Main Entry Screen",
      "route": "/"
    }
  ],
  "repair": "Inspect the user journey and combine these responsibilities when one screen can serve them without duplicating routes or state."
}
```

Multiple features define separate screens for the same likely 'main entry' responsibility. Inspect the user journey and combine these responsibilities when one screen can serve them without duplicating routes or state.

## Current blueprint
```json
{
  "source": {
    "scope_id": "scope_daily_win_d1ec8397",
    "source_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
    "source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53"
  },
  "blueprint_hash": "35bcf19a429ab825eb36836d3caa277ec6a38355b467d36402016992872e9574",
  "assembly": {
    "valid": true,
    "status": "generated_with_issues",
    "errors": [],
    "non_blocking_errors": [
      {
        "code": "cross_feature_table_concept_overlap",
        "severity": "error",
        "blocking": false,
        "category": "database",
        "message": "Multiple features define separate tables for the same likely 'achievement' concept.",
        "affected_feature_ids": [
          "capability_150_character_limit_2a9520cb",
          "capability_record_daily_achievement_86a57805"
        ],
        "components": [
          {
            "feature_id": "capability_150_character_limit_2a9520cb",
            "component_id": "capability_150_character_limit_2a9520cb.table.achievements",
            "name": "f_2a9520cb__achievements"
          },
          {
            "feature_id": "capability_record_daily_achievement_86a57805",
            "component_id": "capability_record_daily_achievement_86a57805.table.achievements",
            "name": "f_86a57805__achievements"
          }
        ],
        "repair": "Inspect whether these tables represent one shared entity. If they do, keep one canonical table and update the affected feature queries and relationships."
      },
      {
        "code": "cross_feature_screen_route_collision",
        "severity": "error",
        "blocking": false,
        "category": "frontend",
        "message": "Multiple features define screens for the same route '/'.",
        "affected_feature_ids": [
          "capability_150_character_limit_2a9520cb",
          "capability_brief_microcopy_76537cc2",
          "capability_confirmation_message_23ce028f",
          "capability_current_date_display_67c458ab",
          "capability_duplicate_entry_prevention_00baa1bc",
          "capability_local_browser_storage_99d93461",
          "capability_non_empty_validation_c7515c58",
          "capability_one_entry_per_day_limit_86f08838",
          "capability_record_daily_achievement_86a57805",
          "capability_save_button_5553765f",
          "capability_single_screen_interface_20b1b421"
        ],
        "components": [
          {
            "feature_id": "capability_150_character_limit_2a9520cb",
            "component_id": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
            "name": "Achievement Entry Screen",
            "route": "/"
          },
          {
            "feature_id": "capability_brief_microcopy_76537cc2",
            "component_id": "capability_brief_microcopy_76537cc2.screen.microcopy_display",
            "name": "Microcopy Display Screen",
            "route": "/"
          },
          {
            "feature_id": "capability_confirmation_message_23ce028f",
            "component_id": "capability_confirmation_message_23ce028f.screen.main_with_confirmation",
            "name": "Main Screen with Confirmation Message",
            "route": "/"
          },
          {
            "feature_id": "capability_current_date_display_67c458ab",
            "component_id": "capability_current_date_display_67c458ab.screen.main_entry",
            "name": "Main Entry Screen",
            "route": "/"
          },
          {
            "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
            "component_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
            "name": "Main Entry Screen",
            "route": "/"
          },
          {
            "feature_id": "capability_local_browser_storage_99d93461",
            "component_id": "capability_local_browser_storage_99d93461.screen.main",
            "name": "Main Win Entry Screen",
            "route": "/"
          },
          {
            "feature_id": "capability_non_empty_validation_c7515c58",
            "component_id": "capability_non_empty_validation_c7515c58.screen.main_entry",
            "name": "Main Entry Screen with Validation",
            "route": "/"
          },
          {
            "feature_id": "capability_one_entry_per_day_limit_86f08838",
            "component_id": "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry",
            "name": "Daily Win Entry Screen",
            "route": "/"
          },
          {
            "feature_id": "capability_record_daily_achievement_86a57805",
            "component_id": "capability_record_daily_achievement_86a57805.screen.main",
            "name": "Daily Achievement Entry",
            "route": "/"
          },
          {
            "feature_id": "capability_save_button_5553765f",
            "component_id": "capability_save_button_5553765f.screen.main_entry",
            "name": "Main Entry Screen",
            "route": "/"
          },
          {
            "feature_id": "capability_single_screen_interface_20b1b421",
            "component_id": "capability_single_screen_interface_20b1b421.screen.main",
            "name": "Main Recording Screen",
            "route": "/"
          }
        ],
        "repair": "Decide whether these responsibilities belong on one shared screen. Merge the screen behavior or assign distinct routes, then update navigation and actions."
      },
      {
        "code": "cross_feature_screen_concept_overlap",
        "severity": "error",
        "blocking": false,
        "category": "frontend",
        "message": "Multiple features define separate screens for the same likely 'main entry' responsibility.",
        "affected_feature_ids": [
          "capability_current_date_display_67c458ab",
          "capability_duplicate_entry_prevention_00baa1bc",
          "capability_save_button_5553765f"
        ],
        "components": [
          {
            "feature_id": "capability_current_date_display_67c458ab",
            "component_id": "capability_current_date_display_67c458ab.screen.main_entry",
            "name": "Main Entry Screen",
            "route": "/"
          },
          {
            "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
            "component_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
            "name": "Main Entry Screen",
            "route": "/"
          },
          {
            "feature_id": "capability_save_button_5553765f",
            "component_id": "capability_save_button_5553765f.screen.main_entry",
            "name": "Main Entry Screen",
            "route": "/"
          }
        ],
        "repair": "Inspect the user journey and combine these responsibilities when one screen can serve them without duplicating routes or state."
      }
    ],
    "non_blocking_error_count": 3
  },
  "coverage": {
    "valid": true,
    "features": {
      "covered": 12,
      "total": 12
    },
    "acceptance_criteria": {
      "covered": 34,
      "total": 34
    }
  },
  "features": [
    {
      "feature_id": "capability_local_browser_storage_99d93461",
      "verification": {
        "valid": true,
        "feature_id": "capability_local_browser_storage_99d93461",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_a_saved_win_is_stored_in_browser_local_7128f533",
            "table_ids": [
              "capability_local_browser_storage_99d93461.table.wins"
            ],
            "function_ids": [
              "capability_local_browser_storage_99d93461.function.save_win",
              "capability_local_browser_storage_99d93461.function.check_win_exists_for_date"
            ],
            "screen_ids": [
              "capability_local_browser_storage_99d93461.screen.main"
            ]
          },
          {
            "criterion_id": "criterion_done_when_clearing_browser_data_removes_the_save_85bf703f",
            "table_ids": [
              "capability_local_browser_storage_99d93461.table.wins"
            ],
            "function_ids": [],
            "screen_ids": [
              "capability_local_browser_storage_99d93461.screen.main"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_stored_win_can_be_retrieved_on_sub_ce2e4e1a",
            "table_ids": [
              "capability_local_browser_storage_99d93461.table.wins"
            ],
            "function_ids": [
              "capability_local_browser_storage_99d93461.function.get_wins"
            ],
            "screen_ids": [
              "capability_local_browser_storage_99d93461.screen.main"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_local_browser_storage_99d93461.screen.main",
            "action_id": "capability_local_browser_storage_99d93461.screen-action.load_today_win",
            "function_id": "capability_local_browser_storage_99d93461.function.get_wins",
            "table_ids": [
              "capability_local_browser_storage_99d93461.table.wins"
            ]
          },
          {
            "screen_id": "capability_local_browser_storage_99d93461.screen.main",
            "action_id": "capability_local_browser_storage_99d93461.screen-action.check_today_entry",
            "function_id": "capability_local_browser_storage_99d93461.function.check_win_exists_for_date",
            "table_ids": [
              "capability_local_browser_storage_99d93461.table.wins"
            ]
          },
          {
            "screen_id": "capability_local_browser_storage_99d93461.screen.main",
            "action_id": "capability_local_browser_storage_99d93461.screen-action.save_achievement",
            "function_id": "capability_local_browser_storage_99d93461.function.save_win",
            "table_ids": [
              "capability_local_browser_storage_99d93461.table.wins",
              "capability_local_browser_storage_99d93461.table.wins"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_device_timezone_detection_aca07cc7",
      "verification": {
        "valid": true,
        "feature_id": "capability_device_timezone_detection_aca07cc7",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_entries_are_associated_with_the_local__ad030689",
            "table_ids": [
              "capability_device_timezone_detection_aca07cc7.table.entry_local_dates"
            ],
            "function_ids": [
              "capability_device_timezone_detection_aca07cc7.function.check_entry_exists_for_date",
              "capability_device_timezone_detection_aca07cc7.function.record_entry_local_date"
            ],
            "screen_ids": [
              "capability_device_timezone_detection_aca07cc7.screen.timezone_detection_service"
            ]
          },
          {
            "criterion_id": "criterion_done_when_midnight_rollover_uses_the_device_s_lo_b1d856ac",
            "table_ids": [
              "capability_device_timezone_detection_aca07cc7.table.entry_local_dates"
            ],
            "function_ids": [
              "capability_device_timezone_detection_aca07cc7.function.check_entry_exists_for_date",
              "capability_device_timezone_detection_aca07cc7.function.record_entry_local_date"
            ],
            "screen_ids": [
              "capability_device_timezone_detection_aca07cc7.screen.timezone_detection_service"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_app_reads_the_device_s_local_calen_14484f00",
            "table_ids": [
              "capability_device_timezone_detection_aca07cc7.table.entry_local_dates"
            ],
            "function_ids": [
              "capability_device_timezone_detection_aca07cc7.function.get_current_local_date"
            ],
            "screen_ids": [
              "capability_device_timezone_detection_aca07cc7.screen.timezone_detection_service"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_device_timezone_detection_aca07cc7.screen.timezone_detection_service",
            "action_id": "capability_device_timezone_detection_aca07cc7.screen-action.get_local_date",
            "function_id": "capability_device_timezone_detection_aca07cc7.function.get_current_local_date",
            "table_ids": []
          },
          {
            "screen_id": "capability_device_timezone_detection_aca07cc7.screen.timezone_detection_service",
            "action_id": "capability_device_timezone_detection_aca07cc7.screen-action.check_date_entry",
            "function_id": "capability_device_timezone_detection_aca07cc7.function.check_entry_exists_for_date",
            "table_ids": [
              "capability_device_timezone_detection_aca07cc7.table.entry_local_dates"
            ]
          },
          {
            "screen_id": "capability_device_timezone_detection_aca07cc7.screen.timezone_detection_service",
            "action_id": "capability_device_timezone_detection_aca07cc7.screen-action.record_date",
            "function_id": "capability_device_timezone_detection_aca07cc7.function.record_entry_local_date",
            "table_ids": [
              "capability_device_timezone_detection_aca07cc7.table.entry_local_dates"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_record_daily_achievement_86a57805",
      "verification": {
        "valid": true,
        "feature_id": "capability_record_daily_achievement_86a57805",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_a_text_input_field_is_visible_on_the_s_98455205",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_record_daily_achievement_86a57805.screen.main"
            ]
          },
          {
            "criterion_id": "criterion_done_when_i_can_type_plain_text_into_the_field_771f2c73",
            "table_ids": [
              "capability_record_daily_achievement_86a57805.table.achievements"
            ],
            "function_ids": [
              "capability_record_daily_achievement_86a57805.function.save_achievement"
            ],
            "screen_ids": [
              "capability_record_daily_achievement_86a57805.screen.main"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_field_accepts_input_up_to_150_char_9078bdb3",
            "table_ids": [
              "capability_record_daily_achievement_86a57805.table.achievements"
            ],
            "function_ids": [
              "capability_record_daily_achievement_86a57805.function.save_achievement"
            ],
            "screen_ids": [
              "capability_record_daily_achievement_86a57805.screen.main"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_record_daily_achievement_86a57805.screen.main",
            "action_id": "capability_record_daily_achievement_86a57805.screen-action.check_existing_entry",
            "function_id": "capability_record_daily_achievement_86a57805.function.check_today_entry",
            "table_ids": [
              "capability_record_daily_achievement_86a57805.table.achievements"
            ]
          },
          {
            "screen_id": "capability_record_daily_achievement_86a57805.screen.main",
            "action_id": "capability_record_daily_achievement_86a57805.screen-action.save_daily_achievement",
            "function_id": "capability_record_daily_achievement_86a57805.function.save_achievement",
            "table_ids": [
              "capability_record_daily_achievement_86a57805.table.achievements",
              "capability_record_daily_achievement_86a57805.table.achievements"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_one_entry_per_day_limit_86f08838",
      "verification": {
        "valid": true,
        "feature_id": "capability_one_entry_per_day_limit_86f08838",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_only_one_win_per_calendar_date_can_be__98e5ed9d",
            "table_ids": [
              "capability_one_entry_per_day_limit_86f08838.table.daily_win_entries"
            ],
            "function_ids": [
              "capability_one_entry_per_day_limit_86f08838.function.check_entry_exists_for_date",
              "capability_one_entry_per_day_limit_86f08838.function.create_daily_win_entry",
              "capability_one_entry_per_day_limit_86f08838.function.get_entry_for_date"
            ],
            "screen_ids": [
              "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_app_checks_storage_for_an_existing_c3e54f9a",
            "table_ids": [
              "capability_one_entry_per_day_limit_86f08838.table.daily_win_entries"
            ],
            "function_ids": [
              "capability_one_entry_per_day_limit_86f08838.function.check_entry_exists_for_date",
              "capability_one_entry_per_day_limit_86f08838.function.create_daily_win_entry",
              "capability_one_entry_per_day_limit_86f08838.function.get_entry_for_date"
            ],
            "screen_ids": [
              "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_limit_resets_at_midnight_2ac01402",
            "table_ids": [
              "capability_one_entry_per_day_limit_86f08838.table.daily_win_entries"
            ],
            "function_ids": [
              "capability_one_entry_per_day_limit_86f08838.function.create_daily_win_entry"
            ],
            "screen_ids": [
              "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry",
            "action_id": "capability_one_entry_per_day_limit_86f08838.screen-action.check_today_entry_on_load",
            "function_id": "capability_one_entry_per_day_limit_86f08838.function.get_entry_for_date",
            "table_ids": [
              "capability_one_entry_per_day_limit_86f08838.table.daily_win_entries"
            ]
          },
          {
            "screen_id": "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry",
            "action_id": "capability_one_entry_per_day_limit_86f08838.screen-action.save_daily_win",
            "function_id": "capability_one_entry_per_day_limit_86f08838.function.create_daily_win_entry",
            "table_ids": [
              "capability_one_entry_per_day_limit_86f08838.table.daily_win_entries",
              "capability_one_entry_per_day_limit_86f08838.table.daily_win_entries"
            ]
          },
          {
            "screen_id": "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry",
            "action_id": "capability_one_entry_per_day_limit_86f08838.screen-action.verify_no_duplicate",
            "function_id": "capability_one_entry_per_day_limit_86f08838.function.check_entry_exists_for_date",
            "table_ids": [
              "capability_one_entry_per_day_limit_86f08838.table.daily_win_entries"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_save_button_5553765f",
      "verification": {
        "valid": true,
        "feature_id": "capability_save_button_5553765f",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_a_clearly_labeled_save_button_is_visib_c700ce7c",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_save_button_5553765f.screen.main_entry"
            ]
          },
          {
            "criterion_id": "criterion_done_when_clicking_the_button_triggers_the_save__c040cec3",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_save_button_5553765f.screen.main_entry"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_button_is_accessible_via_keyboard_1c80aeca",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_save_button_5553765f.screen.main_entry"
            ]
          }
        ],
        "traces": [],
        "errors": []
      }
    },
    {
      "feature_id": "capability_single_screen_interface_20b1b421",
      "verification": {
        "valid": true,
        "feature_id": "capability_single_screen_interface_20b1b421",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_no_additional_screens_or_navigation_el_27d0da88",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_single_screen_interface_20b1b421.screen.main"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_app_opens_directly_to_the_recordin_c3f4a379",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_single_screen_interface_20b1b421.screen.main"
            ]
          }
        ],
        "traces": [],
        "errors": []
      }
    },
    {
      "feature_id": "capability_non_empty_validation_c7515c58",
      "verification": {
        "valid": true,
        "feature_id": "capability_non_empty_validation_c7515c58",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_attempting_to_save_with_an_empty_field_e0ca77bc",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_non_empty_validation_c7515c58.screen.main_entry"
            ]
          },
          {
            "criterion_id": "criterion_done_when_no_empty_entries_are_stored_b60a1975",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_non_empty_validation_c7515c58.screen.main_entry"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_error_message_is_clear_and_support_90a88449",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_non_empty_validation_c7515c58.screen.main_entry"
            ]
          }
        ],
        "traces": [],
        "errors": []
      }
    },
    {
      "feature_id": "capability_150_character_limit_2a9520cb",
      "verification": {
        "valid": true,
        "feature_id": "capability_150_character_limit_2a9520cb",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_the_character_count_is_enforced_before_0dbf8a66",
            "table_ids": [
              "capability_150_character_limit_2a9520cb.table.achievements"
            ],
            "function_ids": [
              "capability_150_character_limit_2a9520cb.function.validate_achievement_text",
              "capability_150_character_limit_2a9520cb.function.create_achievement",
              "capability_150_character_limit_2a9520cb.function.get_achievement_by_date"
            ],
            "screen_ids": [
              "capability_150_character_limit_2a9520cb.screen.achievement_entry",
              "capability_150_character_limit_2a9520cb.screen.achievement_confirmation"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_input_field_prevents_typing_beyond_a1dcbba6",
            "table_ids": [
              "capability_150_character_limit_2a9520cb.table.achievements"
            ],
            "function_ids": [
              "capability_150_character_limit_2a9520cb.function.create_achievement"
            ],
            "screen_ids": [
              "capability_150_character_limit_2a9520cb.screen.achievement_entry"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
            "action_id": "capability_150_character_limit_2a9520cb.screen-action.validate_text_length",
            "function_id": "capability_150_character_limit_2a9520cb.function.validate_achievement_text",
            "table_ids": []
          },
          {
            "screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
            "action_id": "capability_150_character_limit_2a9520cb.screen-action.save_achievement",
            "function_id": "capability_150_character_limit_2a9520cb.function.create_achievement",
            "table_ids": [
              "capability_150_character_limit_2a9520cb.table.achievements",
              "capability_150_character_limit_2a9520cb.table.achievements"
            ]
          },
          {
            "screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
            "action_id": "capability_150_character_limit_2a9520cb.screen-action.check_existing_entry",
            "function_id": "capability_150_character_limit_2a9520cb.function.get_achievement_by_date",
            "table_ids": [
              "capability_150_character_limit_2a9520cb.table.achievements"
            ]
          },
          {
            "screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_confirmation",
            "action_id": "capability_150_character_limit_2a9520cb.screen-action.load_saved_achievement",
            "function_id": "capability_150_character_limit_2a9520cb.function.get_achievement_by_date",
            "table_ids": [
              "capability_150_character_limit_2a9520cb.table.achievements"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_current_date_display_67c458ab",
      "verification": {
        "valid": true,
        "feature_id": "capability_current_date_display_67c458ab",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_the_current_calendar_date_is_visible_o_62d36978",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_current_date_display_67c458ab.screen.main_entry"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_date_updates_automatically_at_midn_107d504b",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_current_date_display_67c458ab.screen.main_entry"
            ]
          }
        ],
        "traces": [],
        "errors": []
      }
    },
    {
      "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
      "verification": {
        "valid": true,
        "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_attempting_to_save_a_second_win_for_to_a54cc69f",
            "table_ids": [
              "capability_duplicate_entry_prevention_00baa1bc.table.daily_wins"
            ],
            "function_ids": [
              "capability_duplicate_entry_prevention_00baa1bc.function.check_today_win_exists",
              "capability_duplicate_entry_prevention_00baa1bc.function.create_win_with_duplicate_check"
            ],
            "screen_ids": [
              "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_input_field_is_disabled_after_the__7ef9e148",
            "table_ids": [
              "capability_duplicate_entry_prevention_00baa1bc.table.daily_wins"
            ],
            "function_ids": [
              "capability_duplicate_entry_prevention_00baa1bc.function.check_today_win_exists"
            ],
            "screen_ids": [
              "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_save_button_is_disabled_or_hidden__b99451f9",
            "table_ids": [
              "capability_duplicate_entry_prevention_00baa1bc.table.daily_wins"
            ],
            "function_ids": [
              "capability_duplicate_entry_prevention_00baa1bc.function.check_today_win_exists"
            ],
            "screen_ids": [
              "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
            "action_id": "capability_duplicate_entry_prevention_00baa1bc.screen-action.check_today_status",
            "function_id": "capability_duplicate_entry_prevention_00baa1bc.function.check_today_win_exists",
            "table_ids": [
              "capability_duplicate_entry_prevention_00baa1bc.table.daily_wins"
            ]
          },
          {
            "screen_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
            "action_id": "capability_duplicate_entry_prevention_00baa1bc.screen-action.save_win",
            "function_id": "capability_duplicate_entry_prevention_00baa1bc.function.create_win_with_duplicate_check",
            "table_ids": [
              "capability_duplicate_entry_prevention_00baa1bc.table.daily_wins",
              "capability_duplicate_entry_prevention_00baa1bc.table.daily_wins"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_confirmation_message_23ce028f",
      "verification": {
        "valid": true,
        "feature_id": "capability_confirmation_message_23ce028f",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_a_success_message_displays_after_savin_b3a915c8",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_confirmation_message_23ce028f.screen.main_with_confirmation"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_message_is_visible_and_easy_to_rea_7b29a7a6",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_confirmation_message_23ce028f.screen.main_with_confirmation"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_message_shows_today_s_saved_win_te_57196f87",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_confirmation_message_23ce028f.screen.main_with_confirmation"
            ]
          }
        ],
        "traces": [],
        "errors": []
      }
    },
    {
      "feature_id": "capability_brief_microcopy_76537cc2",
      "verification": {
        "valid": true,
        "feature_id": "capability_brief_microcopy_76537cc2",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_error_messages_are_clear_and_supportiv_46ca2610",
            "table_ids": [
              "capability_brief_microcopy_76537cc2.table.microcopy_strings"
            ],
            "function_ids": [
              "capability_brief_microcopy_76537cc2.function.get_microcopy_strings",
              "capability_brief_microcopy_76537cc2.function.initialize_microcopy_strings"
            ],
            "screen_ids": [
              "capability_brief_microcopy_76537cc2.screen.microcopy_display"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_duplicate_entry_message_reads_toda_9f35ccdc",
            "table_ids": [
              "capability_brief_microcopy_76537cc2.table.microcopy_strings"
            ],
            "function_ids": [
              "capability_brief_microcopy_76537cc2.function.get_microcopy_strings",
              "capability_brief_microcopy_76537cc2.function.initialize_microcopy_strings"
            ],
            "screen_ids": [
              "capability_brief_microcopy_76537cc2.screen.microcopy_display"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_input_prompt_reads_what_is_one_win_5550f457",
            "table_ids": [
              "capability_brief_microcopy_76537cc2.table.microcopy_strings"
            ],
            "function_ids": [
              "capability_brief_microcopy_76537cc2.function.get_microcopy_strings",
              "capability_brief_microcopy_76537cc2.function.initialize_microcopy_strings"
            ],
            "screen_ids": [
              "capability_brief_microcopy_76537cc2.screen.microcopy_display"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_success_message_reads_today_s_win__3fec592e",
            "table_ids": [
              "capability_brief_microcopy_76537cc2.table.microcopy_strings"
            ],
            "function_ids": [
              "capability_brief_microcopy_76537cc2.function.get_microcopy_strings",
              "capability_brief_microcopy_76537cc2.function.initialize_microcopy_strings"
            ],
            "screen_ids": [
              "capability_brief_microcopy_76537cc2.screen.microcopy_display"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_brief_microcopy_76537cc2.screen.microcopy_display",
            "action_id": "capability_brief_microcopy_76537cc2.screen-action.load_microcopy",
            "function_id": "capability_brief_microcopy_76537cc2.function.get_microcopy_strings",
            "table_ids": [
              "capability_brief_microcopy_76537cc2.table.microcopy_strings"
            ]
          }
        ],
        "errors": []
      }
    }
  ]
}
```

## Historical validation attempts
```json
{
  "records": [
    {
      "feature_id": "capability_local_browser_storage_99d93461",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-06 02:43:00",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_local_browser_storage_99d93461",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "5bffd87e694fc984f51da4448dc62e2a30dceeeae5ea3c74acdea3708ceae4c0",
      "created_at": "2026-10-06 02:43:36",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_local_browser_storage_99d93461",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "ed3f0feae3291ec4de2a845af8a10927edfb5fb708b1e10d6aea2ce42548e472",
      "created_at": "2026-10-06 02:44:15",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_device_timezone_detection_aca07cc7",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-06 02:52:47",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_device_timezone_detection_aca07cc7",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "5eacf8ce26c897468349c872a6e793e3c8459793361ef403c5c42e36d042e2bd",
      "created_at": "2026-10-06 02:53:16",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_device_timezone_detection_aca07cc7",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "16694b2cd7517da6beb165ffe06192b6bfd1cdbe3ac3e7a39e0ba779a7205f5a",
      "created_at": "2026-10-06 02:53:39",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_brief_microcopy_76537cc2",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-06 02:55:05",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_brief_microcopy_76537cc2",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "17f22c4ffc4be293aef7ff89a80ae8c6d6681366c49caf56f7fe6c8611b8fec2",
      "created_at": "2026-10-06 02:55:30",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_brief_microcopy_76537cc2",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "84e6acdcb0ffcc0a27779203006dae9006eea8c60c5782b332a4c7efa163107a",
      "created_at": "2026-10-06 02:55:48",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_record_daily_achievement_86a57805",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-06 02:56:52",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_record_daily_achievement_86a57805",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "8fe4de6c695e76aca05efd0a6b372084af9c93241a103651de6ec2968e606235",
      "created_at": "2026-10-06 02:59:54",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_record_daily_achievement_86a57805",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "05af4d8af88c3850d472eefcc6b74e27b017f2c35282e2d221ea8eca16ea59b1",
      "created_at": "2026-10-06 03:00:24",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_one_entry_per_day_limit_86f08838",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-06 03:00:59",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_one_entry_per_day_limit_86f08838",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "ec98f107310cd5d2d49eaaea85d46daa79bd46859fa6bd576f214cbc19bf554d",
      "created_at": "2026-10-06 03:02:12",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_one_entry_per_day_limit_86f08838",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "501f8377d528bc9bbd392df01ed0330b01831e77b5a357445f4226e80518c278",
      "created_at": "2026-10-06 04:35:18",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_save_button_5553765f",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-06 04:35:34",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_save_button_5553765f",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "eb440b9bc4f72f1001231ef57133ed3803b220f9f1396c23df0b907d7dab3d05",
      "created_at": "2026-10-06 04:35:50",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_save_button_5553765f",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "0068dc9f1ae726d17d8c3e9c5318e4cbfc6337737d7475183017cf2817b8ed26",
      "created_at": "2026-10-06 04:36:09",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_non_empty_validation_c7515c58",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-06 04:36:38",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_non_empty_validation_c7515c58",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "f4abacd57d07ffcad584ed4579078b872e7567b33f7536ed44a64b21220c8d4f",
      "created_at": "2026-10-06 04:36:51",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_non_empty_validation_c7515c58",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "0068dc9f1ae726d17d8c3e9c5318e4cbfc6337737d7475183017cf2817b8ed26",
      "created_at": "2026-10-06 04:37:15",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_single_screen_interface_20b1b421",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-06 04:37:47",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_single_screen_interface_20b1b421",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "b11b5141e92d501c5af081e9020a9c2dfcefd5faea326ae03d6bf0ad5815fb83",
      "created_at": "2026-10-07 10:37:07",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_single_screen_interface_20b1b421",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "0068dc9f1ae726d17d8c3e9c5318e4cbfc6337737d7475183017cf2817b8ed26",
      "created_at": "2026-10-07 10:37:24",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_150_character_limit_2a9520cb",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-08 02:43:33",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_150_character_limit_2a9520cb",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "d14b0045056d477f43e014957ca4e15fdb0d979db2cb1a12057b7d96c3b2c235",
      "created_at": "2026-10-08 02:45:32",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_150_character_limit_2a9520cb",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "f2c4f67a3674330a4d6eb83309fb4a6625c2c800e383b0da5225adee4433f900",
      "created_at": "2026-10-08 02:46:07",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_current_date_display_67c458ab",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-08 02:46:30",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_current_date_display_67c458ab",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "08b649cc7c9e0b175499e3974d2cbd3e53d7e1451706bf3ea6f4100929a2f469",
      "created_at": "2026-10-08 02:46:42",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_current_date_display_67c458ab",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "0068dc9f1ae726d17d8c3e9c5318e4cbfc6337737d7475183017cf2817b8ed26",
      "created_at": "2026-10-08 02:46:58",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-08 02:47:23",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "ccaecbdcd395a73c339385d487cccca3b8ae59b1b215799e35226b57a3a00bc0",
      "created_at": "2026-10-08 02:47:49",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "a507a5b7147d714ebd0eca9bb7b0b9b6f2f2ebe062cfab9c050131defb1a3a0f",
      "created_at": "2026-10-08 02:48:16",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_confirmation_message_23ce028f",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-08 02:48:35",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_confirmation_message_23ce028f",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "af15a856ea1f6a2b2dd31634e6e0475d030475500d47acdcdb20d4674c35b528",
      "created_at": "2026-10-08 02:48:49",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_confirmation_message_23ce028f",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "0068dc9f1ae726d17d8c3e9c5318e4cbfc6337737d7475183017cf2817b8ed26",
      "created_at": "2026-10-08 02:49:27",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    }
  ]
}
```

Use feature IDs and the recorded validation details to compare tables, functions and screens. A rejected candidate is not the finalized blueprint. Missing historical details cannot be recovered.
