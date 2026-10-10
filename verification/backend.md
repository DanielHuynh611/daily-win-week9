# Backend verification

Static checks inspect Python syntax, internal import paths, declared routes/functions, file integrity and credential patterns. `database_contract` means the schema file exists; `dependency_resolution` means requirements.txt exists, not that installation succeeded. `file_integrity` is the verifier's aggregate static result. The raw evidence identifies individual errors. The checked-input package hash below covers the files before reports were added.

## Findings and next steps

```json
{
  "finding": "package_python_syntax_invalid:backend/app.py:11"
}
```

Expected parseable Python; the syntax/compile check did not pass. Inspect the reported file and line, correct the syntax, then rerun the recorded command.

## Check evidence and coverage
```json
{
  "schema_version": "assembled-backend-verification",
  "source": {
    "architecture_session_id": "60814e7f-ba9b-4027-aedb-e6ee8b2e6869",
    "architecture_id": "architecture:scope_daily_win_d1ec8397:627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
    "architecture_source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53"
  },
  "package_hash": "98b3ae11f731784ff87ffeec826061540749a2843240604b32c175c3bd2212bc",
  "static_valid": false,
  "passes": {
    "file_integrity": false,
    "imports": true,
    "route_map": true,
    "function_coverage": true,
    "database_contract": true,
    "dependency_resolution": true,
    "secret_scan": "[redacted]"
  },
  "features": {
    "covered": 12,
    "total": 12
  },
  "functions": {
    "covered": 18,
    "total": 18
  },
  "errors": [
    "package_python_syntax_invalid:backend/app.py:11"
  ],
  "warnings": [],
  "report_hash": "5d9b564c7a7860e1137ac5a1b82d7f4923d1940837ce155aa64e18c672d44c9b",
  "not_run": [
    "database execution",
    "dependency installation",
    "application startup",
    "pytest",
    "integration tests",
    "business behavior"
  ]
}
```

## Feature sources
```json
[
  {
    "feature_id": "capability_local_browser_storage_99d93461",
    "state": "complete",
    "architecture_backend_hash": "f562c5289242c09cbb602057efc730c1416dd7d96fc20d6b342131da5b7b181e",
    "database_feature_sql_hash": "60cf1eb082c90a304ffa580ca08d3416e2a9e71b4c21ea9cf170dae8912a979d",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_device_timezone_detection_aca07cc7",
    "state": "complete",
    "architecture_backend_hash": "c79f1f796b749685bbb426f2bc17dad01ec59e56efce7aa59193402abdc55c0e",
    "database_feature_sql_hash": "5e9ab68c60146637f86e1a2486c99fb8f2d510710d1e75deda133049935ee93e",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_record_daily_achievement_86a57805",
    "state": "complete",
    "architecture_backend_hash": "aba86e76039e76b3d119a601f5a7dece7faf7ff8616f9a15c6388442bcdea34e",
    "database_feature_sql_hash": "1c6be76db549e71c2e2f10be933e758557d6a6b814307d2fec66f486546e871e",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_one_entry_per_day_limit_86f08838",
    "state": "complete",
    "architecture_backend_hash": "f6d9d640ea76d9456ca3f15e74eeef95f5ae84a23e7c7ac3ceaf7f9132d17366",
    "database_feature_sql_hash": "a0878df537ce7824f2091486d388654faaf2674a35960d24e3bcdef0e6ec5c81",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_save_button_5553765f",
    "state": "complete",
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "36ff9b4364254d1f04a29067c4759b3d5f30005818603021e8e8acb11ef47906",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_single_screen_interface_20b1b421",
    "state": "complete",
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "78746bcc8230d4ebc354fd1962865b469351695fe6343ba12846e850fdeb3df3",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_non_empty_validation_c7515c58",
    "state": "complete",
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "07e81bcbcad5d1b099dc77954d0a37ae92736163c254bff59b61bdc4dc0a75f9",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_150_character_limit_2a9520cb",
    "state": "complete",
    "architecture_backend_hash": "5fc99e3b11903ea0774f0e9fbd21b252f32bb8cf75209b4246c8ce1d7c309196",
    "database_feature_sql_hash": "84f432fb43d41cec3becdcfc3191189b86ab6de8384efe842b29df44f5dab326",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_current_date_display_67c458ab",
    "state": "complete",
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "7ce7aa6ec2e23e19e5781ca1ef08bd74b78f1978a88a75e461b088e1f2428707",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
    "state": "complete",
    "architecture_backend_hash": "a3ea9ed5987ade110946a772c8b019ee18ac24b2e92858193e0242acc07d45f9",
    "database_feature_sql_hash": "d726298ef0f3eb831f6f3e2e89427cff23588cf70cdaa2d156564836b16a3174",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_confirmation_message_23ce028f",
    "state": "complete",
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "54f93b07f71d604b54d8944e13eeab739db9e55fe1b27875dd98e139e1153809",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_brief_microcopy_76537cc2",
    "state": "complete",
    "architecture_backend_hash": "524a94986ea8b8bca035626bed5386e9e3698d5aaa684e134f00e6828cc6cee7",
    "database_feature_sql_hash": "fe7b4bc858455ad3c88e18f044e07ff95596c30b4dab0502245f996c14297483",
    "last_error_code": null,
    "last_error_details": []
  }
]
```

## Expected feature routes and functions
```json
[
  {
    "feature_id": "capability_local_browser_storage_99d93461",
    "functions": [
      {
        "id": "capability_local_browser_storage_99d93461.function.save_win",
        "name": "save_win",
        "http_method": "POST",
        "route": "/api/capability_local_browser_storage_99d93461/wins",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_local_browser_storage_99d93461.function.get_wins",
        "name": "get_wins",
        "http_method": "GET",
        "route": "/api/capability_local_browser_storage_99d93461/wins",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_local_browser_storage_99d93461.function.check_win_exists_for_date",
        "name": "check_win_exists_for_date",
        "http_method": "GET",
        "route": "/api/capability_local_browser_storage_99d93461/wins/check",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_device_timezone_detection_aca07cc7",
    "functions": [
      {
        "id": "capability_device_timezone_detection_aca07cc7.function.get_current_local_date",
        "name": "get_current_local_date",
        "http_method": "GET",
        "route": "/api/capability_device_timezone_detection_aca07cc7/local-date/current",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_device_timezone_detection_aca07cc7.function.check_entry_exists_for_date",
        "name": "check_entry_exists_for_date",
        "http_method": "POST",
        "route": "/api/capability_device_timezone_detection_aca07cc7/local-date/check",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_device_timezone_detection_aca07cc7.function.record_entry_local_date",
        "name": "record_entry_local_date",
        "http_method": "POST",
        "route": "/api/capability_device_timezone_detection_aca07cc7/local-date/record",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_record_daily_achievement_86a57805",
    "functions": [
      {
        "id": "capability_record_daily_achievement_86a57805.function.check_today_entry",
        "name": "check_today_entry",
        "http_method": "GET",
        "route": "/api/capability_record_daily_achievement_86a57805/achievements/today",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_record_daily_achievement_86a57805.function.save_achievement",
        "name": "save_achievement",
        "http_method": "POST",
        "route": "/api/capability_record_daily_achievement_86a57805/achievements",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_one_entry_per_day_limit_86f08838",
    "functions": [
      {
        "id": "capability_one_entry_per_day_limit_86f08838.function.check_entry_exists_for_date",
        "name": "check_entry_exists_for_date",
        "http_method": "GET",
        "route": "/api/capability_one_entry_per_day_limit_86f08838/daily-wins/check",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_one_entry_per_day_limit_86f08838.function.create_daily_win_entry",
        "name": "create_daily_win_entry",
        "http_method": "POST",
        "route": "/api/capability_one_entry_per_day_limit_86f08838/daily-wins",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_one_entry_per_day_limit_86f08838.function.get_entry_for_date",
        "name": "get_entry_for_date",
        "http_method": "GET",
        "route": "/api/capability_one_entry_per_day_limit_86f08838/daily-wins/{entry_date}",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_save_button_5553765f",
    "functions": []
  },
  {
    "feature_id": "capability_single_screen_interface_20b1b421",
    "functions": []
  },
  {
    "feature_id": "capability_non_empty_validation_c7515c58",
    "functions": []
  },
  {
    "feature_id": "capability_150_character_limit_2a9520cb",
    "functions": [
      {
        "id": "capability_150_character_limit_2a9520cb.function.validate_achievement_text",
        "name": "validate_achievement_text",
        "http_method": "POST",
        "route": "/api/capability_150_character_limit_2a9520cb/achievements/validate",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_150_character_limit_2a9520cb.function.create_achievement",
        "name": "create_achievement",
        "http_method": "POST",
        "route": "/api/capability_150_character_limit_2a9520cb/achievements",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_150_character_limit_2a9520cb.function.get_achievement_by_date",
        "name": "get_achievement_by_date",
        "http_method": "GET",
        "route": "/api/capability_150_character_limit_2a9520cb/achievements/{date}",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_current_date_display_67c458ab",
    "functions": []
  },
  {
    "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
    "functions": [
      {
        "id": "capability_duplicate_entry_prevention_00baa1bc.function.check_today_win_exists",
        "name": "check_today_win_exists",
        "http_method": "GET",
        "route": "/api/capability_duplicate_entry_prevention_00baa1bc/wins/check-today",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_duplicate_entry_prevention_00baa1bc.function.create_win_with_duplicate_check",
        "name": "create_win_with_duplicate_check",
        "http_method": "POST",
        "route": "/api/capability_duplicate_entry_prevention_00baa1bc/wins",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_confirmation_message_23ce028f",
    "functions": []
  },
  {
    "feature_id": "capability_brief_microcopy_76537cc2",
    "functions": [
      {
        "id": "capability_brief_microcopy_76537cc2.function.get_microcopy_strings",
        "name": "get_microcopy_strings",
        "http_method": "GET",
        "route": "/api/capability_brief_microcopy_76537cc2/microcopy",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_brief_microcopy_76537cc2.function.initialize_microcopy_strings",
        "name": "initialize_microcopy_strings",
        "http_method": "POST",
        "route": "/api/admin/microcopy/initialize",
        "trigger_type": "background"
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
  "stage": "backend feature",
  "feature": "capability_local_browser_storage_99d93461",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/local_browser_storage/feature.py",
          "sha256": "70951ed669470aa667ad316effad0aa3c2588b5be8b79dbf88f9fbe239ae388f"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_local_browser_storage_99d93461",
        "file_count": 1,
        "function_ids": [
          "capability_local_browser_storage_99d93461.function.check_win_exists_for_date",
          "capability_local_browser_storage_99d93461.function.get_wins",
          "capability_local_browser_storage_99d93461.function.save_win"
        ],
        "function_names": [
          "check_win_exists_for_date",
          "get_wins",
          "save_win"
        ],
        "route_count": 3,
        "verification_hash": "0eca217e700c2422d51701090f48b9c46e7905bb6a16ce95ec6d3464a9fcd002"
      }
    }
  ],
  "started_at": "2026-10-08T02:55:17.120822+00:00",
  "workspace_id": "e96c58ee-23fb-4607-ac5d-13350e4b4141",
  "feature_id": "capability_local_browser_storage_99d93461",
  "screen_id": null,
  "expected_workspace_version": 1,
  "session_id": "61681c31-815c-4f3c-8207-27210e739aaa",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_backend_hash": "f562c5289242c09cbb602057efc730c1416dd7d96fc20d6b342131da5b7b181e",
    "database_feature_sql_hash": "60cf1eb082c90a304ffa580ca08d3416e2a9e71b4c21ea9cf170dae8912a979d"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T02:55:34.270866+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_device_timezone_detection_aca07cc7",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/device_timezone_detection/feature.py",
          "sha256": "ca3786d3e5aeeb95098bfa0b802fe15756fd00c624569efcadbdaff09ab0654a"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_device_timezone_detection_aca07cc7",
        "file_count": 1,
        "function_ids": [
          "capability_device_timezone_detection_aca07cc7.function.check_entry_exists_for_date",
          "capability_device_timezone_detection_aca07cc7.function.get_current_local_date",
          "capability_device_timezone_detection_aca07cc7.function.record_entry_local_date"
        ],
        "function_names": [
          "check_entry_exists_for_date",
          "get_current_local_date",
          "record_entry_local_date"
        ],
        "route_count": 3,
        "verification_hash": "b39247f4ffcebb186ef4dc392b18f26f7f248d0ae50af5951d2574dfb4b0f8e3"
      }
    }
  ],
  "started_at": "2026-10-08T02:55:42.268225+00:00",
  "workspace_id": "e96c58ee-23fb-4607-ac5d-13350e4b4141",
  "feature_id": "capability_device_timezone_detection_aca07cc7",
  "screen_id": null,
  "expected_workspace_version": 3,
  "session_id": "61681c31-815c-4f3c-8207-27210e739aaa",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_backend_hash": "c79f1f796b749685bbb426f2bc17dad01ec59e56efce7aa59193402abdc55c0e",
    "database_feature_sql_hash": "5e9ab68c60146637f86e1a2486c99fb8f2d510710d1e75deda133049935ee93e"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T02:56:00.450723+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_record_daily_achievement_86a57805",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/record_daily_achievement/feature.py",
          "sha256": "5a9fc3b044a6ade7229af4dd60470cd279faa89b41192f41dea943806827a007"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_record_daily_achievement_86a57805",
        "file_count": 1,
        "function_ids": [
          "capability_record_daily_achievement_86a57805.function.check_today_entry",
          "capability_record_daily_achievement_86a57805.function.save_achievement"
        ],
        "function_names": [
          "check_today_entry",
          "save_achievement"
        ],
        "route_count": 2,
        "verification_hash": "ca8ec7a52b47309d29b3f2a4c5f22bb67328e371c1e94ab77b542c6fc7755664"
      }
    }
  ],
  "started_at": "2026-10-08T02:56:09.445505+00:00",
  "workspace_id": "e96c58ee-23fb-4607-ac5d-13350e4b4141",
  "feature_id": "capability_record_daily_achievement_86a57805",
  "screen_id": null,
  "expected_workspace_version": 5,
  "session_id": "61681c31-815c-4f3c-8207-27210e739aaa",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_backend_hash": "aba86e76039e76b3d119a601f5a7dece7faf7ff8616f9a15c6388442bcdea34e",
    "database_feature_sql_hash": "1c6be76db549e71c2e2f10be933e758557d6a6b814307d2fec66f486546e871e"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T02:56:21.537702+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_one_entry_per_day_limit_86f08838",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/one_entry_per_day_limit/feature.py",
          "sha256": "cdf4598948f2496c37bb10a8e30e07599614815c6347fcaf575fdc3922eebe95"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_one_entry_per_day_limit_86f08838",
        "file_count": 1,
        "function_ids": [
          "capability_one_entry_per_day_limit_86f08838.function.check_entry_exists_for_date",
          "capability_one_entry_per_day_limit_86f08838.function.create_daily_win_entry",
          "capability_one_entry_per_day_limit_86f08838.function.get_entry_for_date"
        ],
        "function_names": [
          "check_entry_exists_for_date",
          "create_daily_win_entry",
          "get_entry_for_date"
        ],
        "route_count": 3,
        "verification_hash": "463efaa8d02ff55c50cc66fb2e8c3b7c399faffdd012d6a849aab005521f41b8"
      }
    }
  ],
  "started_at": "2026-10-08T02:56:24.682179+00:00",
  "workspace_id": "e96c58ee-23fb-4607-ac5d-13350e4b4141",
  "feature_id": "capability_one_entry_per_day_limit_86f08838",
  "screen_id": null,
  "expected_workspace_version": 7,
  "session_id": "61681c31-815c-4f3c-8207-27210e739aaa",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_backend_hash": "f6d9d640ea76d9456ca3f15e74eeef95f5ae84a23e7c7ac3ceaf7f9132d17366",
    "database_feature_sql_hash": "a0878df537ce7824f2091486d388654faaf2674a35960d24e3bcdef0e6ec5c81"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T02:56:45.971783+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_save_button_5553765f",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/save_button/feature.py",
          "sha256": "0fa9fd4162191c23b62e196029561bee6b142746beab62dfdf99e3cdd14cd400"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_save_button_5553765f",
        "file_count": 1,
        "function_ids": [],
        "function_names": [],
        "route_count": 2,
        "verification_hash": "5ca6774446a478ac9a40b0f8b4c88665348f6fb95635d4fadd9dbc9b641b25f6"
      }
    }
  ],
  "started_at": "2026-10-08T02:56:58.124128+00:00",
  "workspace_id": "e96c58ee-23fb-4607-ac5d-13350e4b4141",
  "feature_id": "capability_save_button_5553765f",
  "screen_id": null,
  "expected_workspace_version": 9,
  "session_id": "61681c31-815c-4f3c-8207-27210e739aaa",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "36ff9b4364254d1f04a29067c4759b3d5f30005818603021e8e8acb11ef47906"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T02:57:05.356712+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_single_screen_interface_20b1b421",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/single_screen_interface/feature.py",
          "sha256": "04d83c027edb504383faba58006e48474656fb32127680cb55e332ec7605c818"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_single_screen_interface_20b1b421",
        "file_count": 1,
        "function_ids": [],
        "function_names": [],
        "route_count": 1,
        "verification_hash": "2ffe2746a292c488708dbd6f67486de58628e9623936d24af75e1e1e53460592"
      }
    }
  ],
  "started_at": "2026-10-08T02:57:22.999514+00:00",
  "workspace_id": "e96c58ee-23fb-4607-ac5d-13350e4b4141",
  "feature_id": "capability_single_screen_interface_20b1b421",
  "screen_id": null,
  "expected_workspace_version": 11,
  "session_id": "61681c31-815c-4f3c-8207-27210e739aaa",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "78746bcc8230d4ebc354fd1962865b469351695fe6343ba12846e850fdeb3df3"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T02:57:27.224768+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_non_empty_validation_c7515c58",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/non_empty_validation/feature.py",
          "sha256": "51140f5d9cf6513bf4dd75273e4b95f9be5c18796d38b364305fab30e4a535cf"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_non_empty_validation_c7515c58",
        "file_count": 1,
        "function_ids": [],
        "function_names": [],
        "route_count": 2,
        "verification_hash": "adf24f8900fc695bd66d9732611ab4a8c66f8aa9f25649091bd63463f9479989"
      }
    }
  ],
  "started_at": "2026-10-08T02:57:31.240146+00:00",
  "workspace_id": "e96c58ee-23fb-4607-ac5d-13350e4b4141",
  "feature_id": "capability_non_empty_validation_c7515c58",
  "screen_id": null,
  "expected_workspace_version": 13,
  "session_id": "61681c31-815c-4f3c-8207-27210e739aaa",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "07e81bcbcad5d1b099dc77954d0a37ae92736163c254bff59b61bdc4dc0a75f9"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T02:57:38.257636+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_150_character_limit_2a9520cb",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/150_character_limit/feature.py",
          "sha256": "d580b003291d1a7acfa9c67f6faae5959768917468caf742fc2ebef43b45201a"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_150_character_limit_2a9520cb",
        "file_count": 1,
        "function_ids": [
          "capability_150_character_limit_2a9520cb.function.create_achievement",
          "capability_150_character_limit_2a9520cb.function.get_achievement_by_date",
          "capability_150_character_limit_2a9520cb.function.validate_achievement_text"
        ],
        "function_names": [
          "create_achievement",
          "get_achievement_by_date",
          "validate_achievement_text"
        ],
        "route_count": 3,
        "verification_hash": "18c418b5846b6bceb73071011265cefc8f8ceb01038dfc87980d90df587d6003"
      }
    }
  ],
  "started_at": "2026-10-08T02:57:45.091699+00:00",
  "workspace_id": "e96c58ee-23fb-4607-ac5d-13350e4b4141",
  "feature_id": "capability_150_character_limit_2a9520cb",
  "screen_id": null,
  "expected_workspace_version": 15,
  "session_id": "61681c31-815c-4f3c-8207-27210e739aaa",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_backend_hash": "5fc99e3b11903ea0774f0e9fbd21b252f32bb8cf75209b4246c8ce1d7c309196",
    "database_feature_sql_hash": "84f432fb43d41cec3becdcfc3191189b86ab6de8384efe842b29df44f5dab326"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T02:57:58.455100+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_current_date_display_67c458ab",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/current_date_display/feature.py",
          "sha256": "77886e47aa2135044b235bd1f3604098e82a6426431a4ee67a90b14cb856e5da"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_current_date_display_67c458ab",
        "file_count": 1,
        "function_ids": [],
        "function_names": [],
        "route_count": 1,
        "verification_hash": "5d55d3b619e14bb1961fbee1660d66974af961e19e6b726076be22c5e2b59e25"
      }
    }
  ],
  "started_at": "2026-10-08T02:58:07.391265+00:00",
  "workspace_id": "e96c58ee-23fb-4607-ac5d-13350e4b4141",
  "feature_id": "capability_current_date_display_67c458ab",
  "screen_id": null,
  "expected_workspace_version": 17,
  "session_id": "61681c31-815c-4f3c-8207-27210e739aaa",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "7ce7aa6ec2e23e19e5781ca1ef08bd74b78f1978a88a75e461b088e1f2428707"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T02:58:11.149325+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_confirmation_message_23ce028f",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/confirmation_message/feature.py",
          "sha256": "98dd365e59987e7f5ff490ab0b2ec17bb1547addb3836127667f68ccf0cb4704"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_confirmation_message_23ce028f",
        "file_count": 1,
        "function_ids": [],
        "function_names": [],
        "route_count": 2,
        "verification_hash": "f80fad86d5f7f9af2b615c4cdc29969a65689454c86e20aa50278087ad5f783c"
      }
    }
  ],
  "started_at": "2026-10-08T02:58:17.958634+00:00",
  "workspace_id": "e96c58ee-23fb-4607-ac5d-13350e4b4141",
  "feature_id": "capability_confirmation_message_23ce028f",
  "screen_id": null,
  "expected_workspace_version": 19,
  "session_id": "61681c31-815c-4f3c-8207-27210e739aaa",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "54f93b07f71d604b54d8944e13eeab739db9e55fe1b27875dd98e139e1153809"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T02:58:24.820542+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_duplicate_entry_prevention_00baa1bc",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/duplicate_entry_prevention/feature.py",
          "sha256": "2af07fd4ee6d0bf889fd037fdea5b986de9db469ae2a4e02b15c5350be9ee755"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
        "file_count": 1,
        "function_ids": [
          "capability_duplicate_entry_prevention_00baa1bc.function.check_today_win_exists",
          "capability_duplicate_entry_prevention_00baa1bc.function.create_win_with_duplicate_check"
        ],
        "function_names": [
          "check_today_win_exists",
          "create_win_with_duplicate_check"
        ],
        "route_count": 2,
        "verification_hash": "013bc340b57fb576041752977101c2cc8eb606dfac8904540cf4f297bb9c361b"
      }
    }
  ],
  "started_at": "2026-10-08T02:58:28.344163+00:00",
  "workspace_id": "e96c58ee-23fb-4607-ac5d-13350e4b4141",
  "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
  "screen_id": null,
  "expected_workspace_version": 21,
  "session_id": "61681c31-815c-4f3c-8207-27210e739aaa",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_backend_hash": "a3ea9ed5987ade110946a772c8b019ee18ac24b2e92858193e0242acc07d45f9",
    "database_feature_sql_hash": "d726298ef0f3eb831f6f3e2e89427cff23588cf70cdaa2d156564836b16a3174"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T02:58:44.910878+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_brief_microcopy_76537cc2",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/brief_microcopy/feature.py",
          "sha256": "cbeb8407a1c5dd88c680a2f493dd28fb68c1b459d9771fc39c5578b704e76e4b"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_brief_microcopy_76537cc2",
        "file_count": 1,
        "function_ids": [
          "capability_brief_microcopy_76537cc2.function.get_microcopy_strings",
          "capability_brief_microcopy_76537cc2.function.initialize_microcopy_strings"
        ],
        "function_names": [
          "get_microcopy_strings",
          "initialize_microcopy_strings"
        ],
        "route_count": 2,
        "verification_hash": "369fe4fbf6d14f23a6bbbc0361a0d8f9da3f2c590b8a0a3ca495b7f77d5cdbad"
      }
    }
  ],
  "started_at": "2026-10-08T02:58:48.377060+00:00",
  "workspace_id": "e96c58ee-23fb-4607-ac5d-13350e4b4141",
  "feature_id": "capability_brief_microcopy_76537cc2",
  "screen_id": null,
  "expected_workspace_version": 23,
  "session_id": "61681c31-815c-4f3c-8207-27210e739aaa",
  "mvp_session_id": "e732d593-a128-47a4-9d6e-40c3b982630a",
  "source": {
    "architecture_backend_hash": "524a94986ea8b8bca035626bed5386e9e3698d5aaa684e134f00e6828cc6cee7",
    "database_feature_sql_hash": "fe7b4bc858455ad3c88e18f044e07ff95596c30b4dab0502245f996c14297483"
  },
  "outcome": "completed",
  "finished_at": "2026-10-08T02:59:02.706204+00:00"
}
```
