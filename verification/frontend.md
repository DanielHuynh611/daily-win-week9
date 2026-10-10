# Frontend generation verification

Foundation and screen generation validate their contracts and compiled output. These are not browser interaction or end-to-end business tests. The retained check records below identify successful output by file hash and retain earlier rejection details.

## Packaged screens
```json
[
  {
    "feature_id": "capability_local_browser_storage_99d93461",
    "screen_id": "capability_local_browser_storage_99d93461.screen.main",
    "route": "/",
    "html_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
    "output_hash": null,
    "generation_issues": []
  },
  {
    "feature_id": "capability_device_timezone_detection_aca07cc7",
    "screen_id": "capability_device_timezone_detection_aca07cc7.screen.timezone_detection_service",
    "route": "/internal/timezone-detection",
    "html_path": "frontend/features/device_timezone_detection/timezone_detection_service.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Response component must belong to a data scope"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_device_timezone_detection_aca07cc7.screen.timezone_detection_service",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    ]
  },
  {
    "feature_id": "capability_record_daily_achievement_86a57805",
    "screen_id": "capability_record_daily_achievement_86a57805.screen.main",
    "route": "/",
    "html_path": "frontend/features/record_daily_achievement/daily_achievement_entry.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Response component must belong to a data scope"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_record_daily_achievement_86a57805.screen.main",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    ]
  },
  {
    "feature_id": "capability_one_entry_per_day_limit_86f08838",
    "screen_id": "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry",
    "route": "/",
    "html_path": "frontend/features/one_entry_per_day_limit/daily_win_entry_screen.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_action_input_unavailable",
        "route": "/api/capability_one_entry_per_day_limit_86f08838/daily-wins/{entry_date}",
        "action": "Check for existing entry on screen load",
        "method": "GET",
        "message": "Check for existing entry on screen load was not added because this screen has no source for entry date.",
        "action_id": "capability_one_entry_per_day_limit_86f08838.screen-action.check_today_entry_on_load",
        "resolution": "The screen is complete without this interaction, which is recorded as a generation limitation.",
        "missing_inputs": [
          "entry_date"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_save_button_5553765f",
    "screen_id": "capability_save_button_5553765f.screen.main_entry",
    "route": "/",
    "html_path": "frontend/features/save_button/main_entry_screen.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_save_button_5553765f.screen.main_entry",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    ]
  },
  {
    "feature_id": "capability_single_screen_interface_20b1b421",
    "screen_id": "capability_single_screen_interface_20b1b421.screen.main",
    "route": "/",
    "html_path": "frontend/features/single_screen_interface/main_recording_screen.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_single_screen_interface_20b1b421.screen.main",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    ]
  },
  {
    "feature_id": "capability_non_empty_validation_c7515c58",
    "screen_id": "capability_non_empty_validation_c7515c58.screen.main_entry",
    "route": "/",
    "html_path": "frontend/features/non_empty_validation/main_entry_screen_with_validation.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_non_empty_validation_c7515c58.screen.main_entry",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    ]
  },
  {
    "feature_id": "capability_150_character_limit_2a9520cb",
    "screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
    "route": "/",
    "html_path": "frontend/features/150_character_limit/achievement_entry_screen.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_action_input_unavailable",
        "route": "/api/capability_150_character_limit_2a9520cb/achievements/{date}",
        "action": "Check for existing achievement today",
        "method": "GET",
        "message": "Check for existing achievement today was not added because this screen has no source for date.",
        "action_id": "capability_150_character_limit_2a9520cb.screen-action.check_existing_entry",
        "resolution": "The screen is complete without this interaction, which is recorded as a generation limitation.",
        "missing_inputs": [
          "date"
        ]
      },
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Unreachable nodes or missing actions"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    ]
  },
  {
    "feature_id": "capability_150_character_limit_2a9520cb",
    "screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_confirmation",
    "route": "/confirmation",
    "html_path": "frontend/features/150_character_limit/achievement_confirmation_screen.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_action_input_unavailable",
        "route": "/api/capability_150_character_limit_2a9520cb/achievements/{date}",
        "action": "Load saved achievement for display",
        "method": "GET",
        "message": "Load saved achievement for display was not added because this screen has no source for date.",
        "action_id": "capability_150_character_limit_2a9520cb.screen-action.load_saved_achievement",
        "resolution": "The screen is complete without this interaction, which is recorded as a generation limitation.",
        "missing_inputs": [
          "date"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_current_date_display_67c458ab",
    "screen_id": "capability_current_date_display_67c458ab.screen.main_entry",
    "route": "/",
    "html_path": "frontend/features/current_date_display/main_entry_screen.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_current_date_display_67c458ab.screen.main_entry",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    ]
  },
  {
    "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
    "screen_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
    "route": "/",
    "html_path": "frontend/features/duplicate_entry_prevention/main_entry_screen.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Response component must belong to a data scope"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    ]
  },
  {
    "feature_id": "capability_confirmation_message_23ce028f",
    "screen_id": "capability_confirmation_message_23ce028f.screen.main_with_confirmation",
    "route": "/",
    "html_path": "frontend/features/confirmation_message/main_screen_with_confirmation_message.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_confirmation_message_23ce028f.screen.main_with_confirmation",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    ]
  },
  {
    "feature_id": "capability_brief_microcopy_76537cc2",
    "screen_id": "capability_brief_microcopy_76537cc2.screen.microcopy_display",
    "route": "/",
    "html_path": "frontend/features/brief_microcopy/microcopy_display_screen.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Response component must belong to a data scope"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_brief_microcopy_76537cc2.screen.microcopy_display",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    ]
  }
]
```

## Logged screen limitations
```json
[
  {
    "feature_id": "capability_device_timezone_detection_aca07cc7",
    "screen_id": "capability_device_timezone_detection_aca07cc7.screen.timezone_detection_service",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Response component must belong to a data scope"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_device_timezone_detection_aca07cc7.screen.timezone_detection_service",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    ]
  },
  {
    "feature_id": "capability_record_daily_achievement_86a57805",
    "screen_id": "capability_record_daily_achievement_86a57805.screen.main",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Response component must belong to a data scope"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_record_daily_achievement_86a57805.screen.main",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    ]
  },
  {
    "feature_id": "capability_one_entry_per_day_limit_86f08838",
    "screen_id": "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry",
    "issues": [
      {
        "code": "frontend_action_input_unavailable",
        "route": "/api/capability_one_entry_per_day_limit_86f08838/daily-wins/{entry_date}",
        "action": "Check for existing entry on screen load",
        "method": "GET",
        "message": "Check for existing entry on screen load was not added because this screen has no source for entry date.",
        "action_id": "capability_one_entry_per_day_limit_86f08838.screen-action.check_today_entry_on_load",
        "resolution": "The screen is complete without this interaction, which is recorded as a generation limitation.",
        "missing_inputs": [
          "entry_date"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_save_button_5553765f",
    "screen_id": "capability_save_button_5553765f.screen.main_entry",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_save_button_5553765f.screen.main_entry",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    ]
  },
  {
    "feature_id": "capability_single_screen_interface_20b1b421",
    "screen_id": "capability_single_screen_interface_20b1b421.screen.main",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_single_screen_interface_20b1b421.screen.main",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    ]
  },
  {
    "feature_id": "capability_non_empty_validation_c7515c58",
    "screen_id": "capability_non_empty_validation_c7515c58.screen.main_entry",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_non_empty_validation_c7515c58.screen.main_entry",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    ]
  },
  {
    "feature_id": "capability_150_character_limit_2a9520cb",
    "screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
    "issues": [
      {
        "code": "frontend_action_input_unavailable",
        "route": "/api/capability_150_character_limit_2a9520cb/achievements/{date}",
        "action": "Check for existing achievement today",
        "method": "GET",
        "message": "Check for existing achievement today was not added because this screen has no source for date.",
        "action_id": "capability_150_character_limit_2a9520cb.screen-action.check_existing_entry",
        "resolution": "The screen is complete without this interaction, which is recorded as a generation limitation.",
        "missing_inputs": [
          "date"
        ]
      },
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Unreachable nodes or missing actions"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    ]
  },
  {
    "feature_id": "capability_150_character_limit_2a9520cb",
    "screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_confirmation",
    "issues": [
      {
        "code": "frontend_action_input_unavailable",
        "route": "/api/capability_150_character_limit_2a9520cb/achievements/{date}",
        "action": "Load saved achievement for display",
        "method": "GET",
        "message": "Load saved achievement for display was not added because this screen has no source for date.",
        "action_id": "capability_150_character_limit_2a9520cb.screen-action.load_saved_achievement",
        "resolution": "The screen is complete without this interaction, which is recorded as a generation limitation.",
        "missing_inputs": [
          "date"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_current_date_display_67c458ab",
    "screen_id": "capability_current_date_display_67c458ab.screen.main_entry",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_current_date_display_67c458ab.screen.main_entry",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    ]
  },
  {
    "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
    "screen_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Response component must belong to a data scope"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    ]
  },
  {
    "feature_id": "capability_confirmation_message_23ce028f",
    "screen_id": "capability_confirmation_message_23ce028f.screen.main_with_confirmation",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_confirmation_message_23ce028f.screen.main_with_confirmation",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    ]
  },
  {
    "feature_id": "capability_brief_microcopy_76537cc2",
    "screen_id": "capability_brief_microcopy_76537cc2.screen.microcopy_display",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Response component must belong to a data scope"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_brief_microcopy_76537cc2.screen.microcopy_display",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    ]
  }
]
```

## Generation and repair history

Failed attempts below are historical, not automatically defects in these files. A matching file hash identifies a checked output retained in this package. Earlier discarded evidence cannot be reconstructed. An empty history does not mean every attempt passed.

### Checked output matches packaged files

```json
{
  "stage": "frontend foundation",
  "feature": null,
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "frontend foundation",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Foundation contract and files",
      "status": "passed",
      "files": [
        {
          "path": "frontend/shared/ui/library.css",
          "sha256": "568a8688dec549949855d47c2f88023690c039c672db98c3129fa98467fd8be2"
        },
        {
          "path": "frontend/shared/ui/library.js",
          "sha256": "6a828731b69d0b0948ae6fa0afb4d52dcce347007e3d5e2fd603170ee27a70dc"
        },
        {
          "path": "frontend/shared/ui/runtime.js",
          "sha256": "166cbf38f4d2cb1166b527ac91445d41f4741e2a2531f4a768034932a77ea0df"
        },
        {
          "path": "frontend/shared/ui/shell.html",
          "sha256": "51d72b3ce6b7543d744ffdd97629e608946ae7cce037751aa589498fa7b24414"
        },
        {
          "path": "frontend/shared/ui/auth.html",
          "sha256": "800e84d26cc057f3ab466cd725d584178e0da8d4a320388ef4d805690d890954"
        },
        {
          "path": "frontend/shared/ui/catalogue.json",
          "sha256": "a7dad497b83ff406316ad3b634bd059c71fc048b32c781ebd0e9a1ca1060347b"
        },
        {
          "path": "frontend/shared/ui/screen-templates.json",
          "sha256": "76c01145d20d88dc2aa96db9685462ec42edf17adfdfff4cd6b6f884de5c5239"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:00:13.934737+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": null,
  "screen_id": null,
  "expected_workspace_version": 1,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_source_hash": "ff87a2d857170be0f340ac73d12d582b3f13e0336022225c066578b974b346ec"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T03:00:14.123026+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_local_browser_storage_99d93461",
  "screen": "capability_local_browser_storage_99d93461.screen.main",
  "outcome": "completed"
}
```

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
          "sha256": "b6596ec684f9e8d95aeb722ee77c5efb1c7c06add89372a284700ce22129e2df"
        },
        {
          "path": "frontend/features/local_browser_storage/main_win_entry_screen.js",
          "sha256": "268aa7e73aa4fde5f2266a32ca0a3b75a8f79e7c956d885f91bc05ee1a178ea0"
        },
        {
          "path": "frontend/features/local_browser_storage/main_win_entry_screen.screen.json",
          "sha256": "fdd6afcd4b4c373164bf52474b65990b21d87adfde7f6f6f073101f591d0cddb"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:00:22.656313+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": "capability_local_browser_storage_99d93461",
  "screen_id": "capability_local_browser_storage_99d93461.screen.main",
  "expected_workspace_version": 2,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_screens_hash": "6a6df517dfc188b089a79c904681dffb23e3d01b0fd205b5d109fb97b6731301",
    "backend_code_hash": "1787625d45b1ccbc1bfb5a657e34f2b177e3a356e40198f3e82d15730dbd66f9",
    "foundation_hash": "b203da38a9bce731d379b51ccbbe1567f784318c352a3d8eb2205e6133d9c06e"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T03:00:32.413345+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_device_timezone_detection_aca07cc7",
  "screen": "capability_device_timezone_detection_aca07cc7.screen.timezone_detection_service",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Response component must belong to a data scope"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_device_timezone_detection_aca07cc7.screen.timezone_detection_service",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Response component must belong to a data scope"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/device_timezone_detection/timezone_detection_service.html",
          "sha256": "a8b8542f4feedf92559e43b947ff641d526e6e375b80da33845681d90f42a8aa"
        },
        {
          "path": "frontend/features/device_timezone_detection/timezone_detection_service.js",
          "sha256": "40678c4de4c4322b06ae50828994a0a3227d56f53416ceaeac8c89df1fa10364"
        },
        {
          "path": "frontend/features/device_timezone_detection/timezone_detection_service.screen.json",
          "sha256": "d0a5d8a694b364f976efcb728e1224478ea114aa1868a5db4736647e161e0fe4"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:00:58.091987+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": "capability_device_timezone_detection_aca07cc7",
  "screen_id": "capability_device_timezone_detection_aca07cc7.screen.timezone_detection_service",
  "expected_workspace_version": 4,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_screens_hash": "cd4f7d8f01cd4b02a306cd6602a100ee8d3c88a831979c539f38b6fcad83d166",
    "backend_code_hash": "4befddbdf29f0f0f249890fd822de1c9bdfe1ed1e00cd0936dac35cc53fcb954",
    "foundation_hash": "b203da38a9bce731d379b51ccbbe1567f784318c352a3d8eb2205e6133d9c06e"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-08T03:01:10.383535+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_record_daily_achievement_86a57805",
  "screen": "capability_record_daily_achievement_86a57805.screen.main",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Response component must belong to a data scope"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_record_daily_achievement_86a57805.screen.main",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Response component must belong to a data scope"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/record_daily_achievement/daily_achievement_entry.html",
          "sha256": "e96d3caf9b319ac3b0afdef8a8d239be9ef97a8398051c66c79e79952c5687e6"
        },
        {
          "path": "frontend/features/record_daily_achievement/daily_achievement_entry.js",
          "sha256": "99076fcee3377b1601eec86789edbf404a0167932164de9bb34887c5665fa10e"
        },
        {
          "path": "frontend/features/record_daily_achievement/daily_achievement_entry.screen.json",
          "sha256": "5326eb35c3a3c9c77baa9fbc9c6fdcfa9fc346e8b6b2db384bcd1eafeaeb0cc0"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:01:35.172403+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": "capability_record_daily_achievement_86a57805",
  "screen_id": "capability_record_daily_achievement_86a57805.screen.main",
  "expected_workspace_version": 6,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_screens_hash": "50eb0dc3efd55c6e8b3285705df196fc1609205da2e0dad41bf1864c1e7fb517",
    "backend_code_hash": "3b81021ec4de8ec4718c830c84f93d482f1e5993b3ecc9b58a41e8922b41b1fd",
    "foundation_hash": "b203da38a9bce731d379b51ccbbe1567f784318c352a3d8eb2205e6133d9c06e"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-08T03:01:45.270676+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_one_entry_per_day_limit_86f08838",
  "screen": "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "frontend_action_input_unavailable"
}
```

A screen action needed a route value that the screen cannot obtain. The usable screen was generated without that action. Use the retained action, route and missing-input details below to correct the upstream contract, then regenerate only this screen.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen action availability",
      "status": "warning",
      "code": "frontend_action_input_unavailable",
      "details": {
        "code": "frontend_action_input_unavailable",
        "action_id": "capability_one_entry_per_day_limit_86f08838.screen-action.check_today_entry_on_load",
        "action": "Check for existing entry on screen load",
        "method": "GET",
        "route": "/api/capability_one_entry_per_day_limit_86f08838/daily-wins/{entry_date}",
        "missing_inputs": [
          "entry_date"
        ],
        "message": "Check for existing entry on screen load was not added because this screen has no source for entry date.",
        "resolution": "The screen is complete without this interaction, which is recorded as a generation limitation."
      }
    },
    {
      "check": "Screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/one_entry_per_day_limit/daily_win_entry_screen.html",
          "sha256": "89a0cedaf2e406166f50d792975d067c687c93ffb783672a0d9c1a31cbc79b76"
        },
        {
          "path": "frontend/features/one_entry_per_day_limit/daily_win_entry_screen.js",
          "sha256": "d9b713c8f53027937f791260f85b6d8861c8096e926c59303892f2736c3bc45e"
        },
        {
          "path": "frontend/features/one_entry_per_day_limit/daily_win_entry_screen.screen.json",
          "sha256": "0c843450875c986c148d9285602bbb8023af31707636d9d09f753968e650f15f"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:01:50.388489+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": "capability_one_entry_per_day_limit_86f08838",
  "screen_id": "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry",
  "expected_workspace_version": 8,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_screens_hash": "f7c25083cb860c2af0cd61fbd046dc2062d869b9812ca3ffe95fe35707e6bdb7",
    "backend_code_hash": "37a79285d375f10359e295ededa258b382a0b94f021afc8f144737077a8c9275",
    "foundation_hash": "b203da38a9bce731d379b51ccbbe1567f784318c352a3d8eb2205e6133d9c06e"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-08T03:02:01.954776+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_save_button_5553765f",
  "screen": "capability_save_button_5553765f.screen.main_entry",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen action availability",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_save_button_5553765f.screen.main_entry",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    },
    {
      "check": "Screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/save_button/main_entry_screen.html",
          "sha256": "d95e4cc06996cf5e5dbf365c8e00e42c338b5152c5bcba37214f42bf6b910ecd"
        },
        {
          "path": "frontend/features/save_button/main_entry_screen.js",
          "sha256": "99076fcee3377b1601eec86789edbf404a0167932164de9bb34887c5665fa10e"
        },
        {
          "path": "frontend/features/save_button/main_entry_screen.screen.json",
          "sha256": "e61f22ce5b93209d25bc767bdd3fff708611a3d75423116b5b462d3aaf310884"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:02:43.392681+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": "capability_save_button_5553765f",
  "screen_id": "capability_save_button_5553765f.screen.main_entry",
  "expected_workspace_version": 10,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_screens_hash": "8b324404df02c7f2ab8c0b9a3dc130ef9c8d569735380c347a9fb5d41f917409",
    "backend_code_hash": "23406c8aa78657cec41c52343f2417261f0bb3e764aff6b203b5399773a59ad0",
    "foundation_hash": "b203da38a9bce731d379b51ccbbe1567f784318c352a3d8eb2205e6133d9c06e"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-08T03:02:43.599984+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_single_screen_interface_20b1b421",
  "screen": "capability_single_screen_interface_20b1b421.screen.main",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen action availability",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_single_screen_interface_20b1b421.screen.main",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    },
    {
      "check": "Screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/single_screen_interface/main_recording_screen.html",
          "sha256": "bdc288479aeb26900bccf6e624da955261a453ac739d610e80441f0815a97c6c"
        },
        {
          "path": "frontend/features/single_screen_interface/main_recording_screen.js",
          "sha256": "99076fcee3377b1601eec86789edbf404a0167932164de9bb34887c5665fa10e"
        },
        {
          "path": "frontend/features/single_screen_interface/main_recording_screen.screen.json",
          "sha256": "a276b253f5d3415a9e4877697320b4c7974b4a90dcd6889924ac6cdca6f84aed"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:02:59.340125+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": "capability_single_screen_interface_20b1b421",
  "screen_id": "capability_single_screen_interface_20b1b421.screen.main",
  "expected_workspace_version": 12,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_screens_hash": "c5957c397c66f39a86f49c4154815229769378e33ee6cb8a9b39a43553da3f96",
    "backend_code_hash": "e415f1e8ccd4e8aafcc3185361e62aedf6e86238e45794a9a5c6cd743fe4dc62",
    "foundation_hash": "b203da38a9bce731d379b51ccbbe1567f784318c352a3d8eb2205e6133d9c06e"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-08T03:02:59.548916+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_non_empty_validation_c7515c58",
  "screen": "capability_non_empty_validation_c7515c58.screen.main_entry",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen action availability",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_non_empty_validation_c7515c58.screen.main_entry",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    },
    {
      "check": "Screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/non_empty_validation/main_entry_screen_with_validation.html",
          "sha256": "a29869e6bf564ff9c812455266dbceb9e5511366a68647f5f6add057579cf356"
        },
        {
          "path": "frontend/features/non_empty_validation/main_entry_screen_with_validation.js",
          "sha256": "99076fcee3377b1601eec86789edbf404a0167932164de9bb34887c5665fa10e"
        },
        {
          "path": "frontend/features/non_empty_validation/main_entry_screen_with_validation.screen.json",
          "sha256": "72413c2e5335da904ad4224071d936f2d61630b60933b116a7eac74ca231aab4"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:03:20.951081+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": "capability_non_empty_validation_c7515c58",
  "screen_id": "capability_non_empty_validation_c7515c58.screen.main_entry",
  "expected_workspace_version": 14,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_screens_hash": "bbb4b01de3ea8aed2397c29ba16bbfeb3af3022051b9d02353993fb5c790cdd5",
    "backend_code_hash": "0bc6345fd04cacb3033a58ac88c1fa94aa39ddb49ccf68507e0d620e48ad56fc",
    "foundation_hash": "b203da38a9bce731d379b51ccbbe1567f784318c352a3d8eb2205e6133d9c06e"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-08T03:03:21.171261+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_150_character_limit_2a9520cb",
  "screen": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "frontend_action_input_unavailable"
}
```

A screen action needed a route value that the screen cannot obtain. The usable screen was generated without that action. Use the retained action, route and missing-input details below to correct the upstream contract, then regenerate only this screen.

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen action availability",
      "status": "warning",
      "code": "frontend_action_input_unavailable",
      "details": {
        "code": "frontend_action_input_unavailable",
        "action_id": "capability_150_character_limit_2a9520cb.screen-action.check_existing_entry",
        "action": "Check for existing achievement today",
        "method": "GET",
        "route": "/api/capability_150_character_limit_2a9520cb/achievements/{date}",
        "missing_inputs": [
          "date"
        ],
        "message": "Check for existing achievement today was not added because this screen has no source for date.",
        "resolution": "The screen is complete without this interaction, which is recorded as a generation limitation."
      }
    },
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Unreachable nodes or missing actions"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Unreachable nodes or missing actions"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/150_character_limit/achievement_entry_screen.html",
          "sha256": "dd38596e32031ebcb8f7029f43acd434479d497927b022321a5e3063e637356b"
        },
        {
          "path": "frontend/features/150_character_limit/achievement_entry_screen.js",
          "sha256": "99076fcee3377b1601eec86789edbf404a0167932164de9bb34887c5665fa10e"
        },
        {
          "path": "frontend/features/150_character_limit/achievement_entry_screen.screen.json",
          "sha256": "702a19b18b50d0c92567d80c664ca7f7955e1898cec1205c9add8280847684e9"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:03:25.945433+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": "capability_150_character_limit_2a9520cb",
  "screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
  "expected_workspace_version": 16,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_screens_hash": "8688e456120508b9805db5676a9f640941d192bd7832a87f9ae8bcb14d618512",
    "backend_code_hash": "738ae82d15c5673d07701ea8a4a63d85b7952c0a84988f504914ec2e914d6afd",
    "foundation_hash": "b203da38a9bce731d379b51ccbbe1567f784318c352a3d8eb2205e6133d9c06e"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-08T03:03:33.283772+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_current_date_display_67c458ab",
  "screen": "capability_current_date_display_67c458ab.screen.main_entry",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen action availability",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_current_date_display_67c458ab.screen.main_entry",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    },
    {
      "check": "Screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/current_date_display/main_entry_screen.html",
          "sha256": "c703698f4f98c3b70e74b93bbd5ee7cec530c852c1ec8502c5939a1726faedff"
        },
        {
          "path": "frontend/features/current_date_display/main_entry_screen.js",
          "sha256": "99076fcee3377b1601eec86789edbf404a0167932164de9bb34887c5665fa10e"
        },
        {
          "path": "frontend/features/current_date_display/main_entry_screen.screen.json",
          "sha256": "346792e7367feac7cc2d57f4ac14a00d2117e3e648ba80d8b14da973d0a3982e"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:04:57.077136+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": "capability_current_date_display_67c458ab",
  "screen_id": "capability_current_date_display_67c458ab.screen.main_entry",
  "expected_workspace_version": 18,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_screens_hash": "4f7c3dedff3d2217fd8e1cb504e519798b13d121210e2acc4bda2a5b070fd665",
    "backend_code_hash": "8d1c86a018ae8a1cafebd9a7995d8066f249aa0b1ac97d19990691f67bc702f9",
    "foundation_hash": "b203da38a9bce731d379b51ccbbe1567f784318c352a3d8eb2205e6133d9c06e"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-08T03:04:57.294703+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_duplicate_entry_prevention_00baa1bc",
  "screen": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Response component must belong to a data scope"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Response component must belong to a data scope"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/duplicate_entry_prevention/main_entry_screen.html",
          "sha256": "e92ef0c7ccaf5ef38c3a8c88f4ebda31bb09ecfe9c40ccaffdc719498651ac27"
        },
        {
          "path": "frontend/features/duplicate_entry_prevention/main_entry_screen.js",
          "sha256": "99076fcee3377b1601eec86789edbf404a0167932164de9bb34887c5665fa10e"
        },
        {
          "path": "frontend/features/duplicate_entry_prevention/main_entry_screen.screen.json",
          "sha256": "9c172898cf56de00afb2cb5676a2f189381cc1590361afd98f15fe50084f7ff6"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:05:03.917717+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
  "screen_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
  "expected_workspace_version": 20,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_screens_hash": "bdffa29ea8fd621a00a2acd9f14cd6a67c96e62e1d2f36da58e0c4adbb618129",
    "backend_code_hash": "80fdd5773fa6e8e35dcbe5fae90b8251a6c69c95f6cc3ac78d9403165883dc26",
    "foundation_hash": "b203da38a9bce731d379b51ccbbe1567f784318c352a3d8eb2205e6133d9c06e"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-08T03:05:13.722263+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_confirmation_message_23ce028f",
  "screen": "capability_confirmation_message_23ce028f.screen.main_with_confirmation",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen action availability",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_confirmation_message_23ce028f.screen.main_with_confirmation",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations."
      }
    },
    {
      "check": "Screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/confirmation_message/main_screen_with_confirmation_message.html",
          "sha256": "60392eafae35f25fe85340384cf8c9c7e9cac5e2e2e6aa4a2f171c524bb9657f"
        },
        {
          "path": "frontend/features/confirmation_message/main_screen_with_confirmation_message.js",
          "sha256": "99076fcee3377b1601eec86789edbf404a0167932164de9bb34887c5665fa10e"
        },
        {
          "path": "frontend/features/confirmation_message/main_screen_with_confirmation_message.screen.json",
          "sha256": "109b1631c14a4787972147f4ec886a3d3eb108004f50e241748572cd47fc682c"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:05:20.970545+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": "capability_confirmation_message_23ce028f",
  "screen_id": "capability_confirmation_message_23ce028f.screen.main_with_confirmation",
  "expected_workspace_version": 22,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_screens_hash": "c1f932079d25f994c31a37b7dffe69589741f5c2a187028a6ba04cb818a136c7",
    "backend_code_hash": "276a054311ed13e08a50e43893b7f37eb61badfc427b97058b948ce3859ea80c",
    "foundation_hash": "b203da38a9bce731d379b51ccbbe1567f784318c352a3d8eb2205e6133d9c06e"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-08T03:05:21.183129+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_brief_microcopy_76537cc2",
  "screen": "capability_brief_microcopy_76537cc2.screen.microcopy_display",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Response component must belong to a data scope"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_brief_microcopy_76537cc2.screen.microcopy_display",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Response component must belong to a data scope"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/brief_microcopy/microcopy_display_screen.html",
          "sha256": "4a301a0396f34b17c27344c186d012676acac27f35c93f2e5e361c593bad9ce6"
        },
        {
          "path": "frontend/features/brief_microcopy/microcopy_display_screen.js",
          "sha256": "99076fcee3377b1601eec86789edbf404a0167932164de9bb34887c5665fa10e"
        },
        {
          "path": "frontend/features/brief_microcopy/microcopy_display_screen.screen.json",
          "sha256": "487e5fdf454d9b347c08913f484cbefaeacf18fc0430d7ab42940ebe51504220"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:05:43.688818+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": "capability_brief_microcopy_76537cc2",
  "screen_id": "capability_brief_microcopy_76537cc2.screen.microcopy_display",
  "expected_workspace_version": 24,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_screens_hash": "6dcc986635cc13410b857182e2dedc11868e869b82345011a120f42c9de4b315",
    "backend_code_hash": "fbd834839626f45b855c31f4cb5b6cfccdb996fe86e053e629082bf00bb9b798",
    "foundation_hash": "b203da38a9bce731d379b51ccbbe1567f784318c352a3d8eb2205e6133d9c06e"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-08T03:05:51.173366+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_150_character_limit_2a9520cb",
  "screen": "capability_150_character_limit_2a9520cb.screen.achievement_confirmation",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "frontend_action_input_unavailable"
}
```

A screen action needed a route value that the screen cannot obtain. The usable screen was generated without that action. Use the retained action, route and missing-input details below to correct the upstream contract, then regenerate only this screen.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen action availability",
      "status": "warning",
      "code": "frontend_action_input_unavailable",
      "details": {
        "code": "frontend_action_input_unavailable",
        "action_id": "capability_150_character_limit_2a9520cb.screen-action.load_saved_achievement",
        "action": "Load saved achievement for display",
        "method": "GET",
        "route": "/api/capability_150_character_limit_2a9520cb/achievements/{date}",
        "missing_inputs": [
          "date"
        ],
        "message": "Load saved achievement for display was not added because this screen has no source for date.",
        "resolution": "The screen is complete without this interaction, which is recorded as a generation limitation."
      }
    },
    {
      "check": "Screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/150_character_limit/achievement_confirmation_screen.html",
          "sha256": "eb0ebccec2ee9f3afbe3ec44d34e8ce3ccde6173fffe8bde05c5e1757ddeee3f"
        },
        {
          "path": "frontend/features/150_character_limit/achievement_confirmation_screen.js",
          "sha256": "4347c02576bcfa47cf74ed8e484c38bcc74ca3c8210d680dd1b47052b17952fc"
        },
        {
          "path": "frontend/features/150_character_limit/achievement_confirmation_screen.screen.json",
          "sha256": "017dc306cc47e7b8315adeddc47d4a77d228332eca089b7bb028f2208345d4e6"
        }
      ]
    }
  ],
  "started_at": "2026-10-08T03:07:16.301209+00:00",
  "workspace_id": "fc3bc5ae-1b35-4cb8-9a19-7a12957b350f",
  "feature_id": "capability_150_character_limit_2a9520cb",
  "screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_confirmation",
  "expected_workspace_version": 26,
  "session_id": "b983ca54-5aae-4431-bd2b-8fc01b532599",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_screens_hash": "8688e456120508b9805db5676a9f640941d192bd7832a87f9ae8bcb14d618512",
    "backend_code_hash": "738ae82d15c5673d07701ea8a4a63d85b7952c0a84988f504914ec2e914d6afd",
    "foundation_hash": "b203da38a9bce731d379b51ccbbe1567f784318c352a3d8eb2205e6133d9c06e"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-08T03:07:16.505027+00:00"
}
```
