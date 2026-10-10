# Database verification

SQL assembly concatenates the approved feature SQL into `database/schema.sql`. Generation checks table coverage and SQL structure; it does not execute the schema against MySQL. Constraints, migrations and queries have not been proven by these checks.

```json
{
  "records": [
    {
      "session_id": "463a8da5-8e9e-40c4-a4a7-486ec8c71e52",
      "source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
      "state": "completed",
      "manifest_hash": "31022ce5d639b0974464e387e5e40713ba0fa1e0b1457b5b290f421932d711ac"
    }
  ]
}
```

## Current SQL revisions

```json
{
  "records": [
    {
      "feature_id": "capability_local_browser_storage_99d93461",
      "state": "approved",
      "revision": 1,
      "last_run_id": "6572d656-96a0-42ed-8ca5-7c47b16e4dc0",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_device_timezone_detection_aca07cc7",
      "state": "approved",
      "revision": 1,
      "last_run_id": "69c2e6c6-81ec-416f-ba38-fdfc6ffd0981",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_record_daily_achievement_86a57805",
      "state": "approved",
      "revision": 1,
      "last_run_id": "272e2685-c655-4c93-b240-142adceaa4d7",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_one_entry_per_day_limit_86f08838",
      "state": "approved",
      "revision": 1,
      "last_run_id": "ccb90036-f5c7-4a14-98ad-d8459acadf4f",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_save_button_5553765f",
      "state": "approved",
      "revision": 1,
      "last_run_id": "9ff0e181-5bfd-4c1b-ab47-0bc23acd4373",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_single_screen_interface_20b1b421",
      "state": "approved",
      "revision": 1,
      "last_run_id": "c9de3321-9bfe-44f0-a3bc-1da62d5b9146",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_non_empty_validation_c7515c58",
      "state": "approved",
      "revision": 1,
      "last_run_id": "b3a1f6c4-3f1a-4dd4-bb6b-bb4ede80085f",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_150_character_limit_2a9520cb",
      "state": "approved",
      "revision": 1,
      "last_run_id": "8355904f-ec2b-4238-b68b-8fc3f6c1dde6",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_current_date_display_67c458ab",
      "state": "approved",
      "revision": 1,
      "last_run_id": "42665e3e-613d-42b1-902d-55d2dbbd4782",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_duplicate_entry_prevention_00baa1bc",
      "state": "approved",
      "revision": 1,
      "last_run_id": "390bdb3d-8916-4f7f-8c3f-50efe1408174",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_confirmation_message_23ce028f",
      "state": "approved",
      "revision": 1,
      "last_run_id": "683f67f0-95a2-4eef-afa5-2120be31c508",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_brief_microcopy_76537cc2",
      "state": "approved",
      "revision": 1,
      "last_run_id": "eba8b5ed-d399-4148-a679-b026fc9e3850",
      "last_error_code": null,
      "last_error_details": null
    }
  ]
}
```

## Run history
Compare each feature's last_run_id with these run IDs. Failed/superseded runs are historical; compare source hashes.

```json
{
  "records": [
    {
      "id": "6572d656-96a0-42ed-8ca5-7c47b16e4dc0",
      "scope_key": "feature:capability_local_browser_storage_99d93461",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
      "created_at": "2026-10-08 02:50:10",
      "finished_at": "2026-10-08 02:50:14",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 3537,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "69c2e6c6-81ec-416f-ba38-fdfc6ffd0981",
      "scope_key": "feature:capability_device_timezone_detection_aca07cc7",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
      "created_at": "2026-10-08 02:50:20",
      "finished_at": "2026-10-08 02:50:23",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 3665,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "272e2685-c655-4c93-b240-142adceaa4d7",
      "scope_key": "feature:capability_record_daily_achievement_86a57805",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
      "created_at": "2026-10-08 02:50:27",
      "finished_at": "2026-10-08 02:50:30",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 2747,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "ccb90036-f5c7-4a14-98ad-d8459acadf4f",
      "scope_key": "feature:capability_one_entry_per_day_limit_86f08838",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
      "created_at": "2026-10-08 02:50:35",
      "finished_at": "2026-10-08 02:50:39",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 3845,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "9ff0e181-5bfd-4c1b-ab47-0bc23acd4373",
      "scope_key": "feature:capability_save_button_5553765f",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
      "created_at": "2026-10-08 02:50:44",
      "finished_at": "2026-10-08 02:50:44",
      "error_code": null,
      "error_details": [],
      "provider_attempts": []
    },
    {
      "id": "c9de3321-9bfe-44f0-a3bc-1da62d5b9146",
      "scope_key": "feature:capability_single_screen_interface_20b1b421",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
      "created_at": "2026-10-08 02:50:47",
      "finished_at": "2026-10-08 02:50:47",
      "error_code": null,
      "error_details": [],
      "provider_attempts": []
    },
    {
      "id": "b3a1f6c4-3f1a-4dd4-bb6b-bb4ede80085f",
      "scope_key": "feature:capability_non_empty_validation_c7515c58",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
      "created_at": "2026-10-08 02:50:51",
      "finished_at": "2026-10-08 02:50:51",
      "error_code": null,
      "error_details": [],
      "provider_attempts": []
    },
    {
      "id": "8355904f-ec2b-4238-b68b-8fc3f6c1dde6",
      "scope_key": "feature:capability_150_character_limit_2a9520cb",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
      "created_at": "2026-10-08 02:50:56",
      "finished_at": "2026-10-08 02:51:00",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 3688,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "42665e3e-613d-42b1-902d-55d2dbbd4782",
      "scope_key": "feature:capability_current_date_display_67c458ab",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
      "created_at": "2026-10-08 02:51:06",
      "finished_at": "2026-10-08 02:51:07",
      "error_code": null,
      "error_details": [],
      "provider_attempts": []
    },
    {
      "id": "390bdb3d-8916-4f7f-8c3f-50efe1408174",
      "scope_key": "feature:capability_duplicate_entry_prevention_00baa1bc",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
      "created_at": "2026-10-08 02:51:11",
      "finished_at": "2026-10-08 02:51:14",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 2510,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "683f67f0-95a2-4eef-afa5-2120be31c508",
      "scope_key": "feature:capability_confirmation_message_23ce028f",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
      "created_at": "2026-10-08 02:51:19",
      "finished_at": "2026-10-08 02:51:20",
      "error_code": null,
      "error_details": [],
      "provider_attempts": []
    },
    {
      "id": "eba8b5ed-d399-4148-a679-b026fc9e3850",
      "scope_key": "feature:capability_brief_microcopy_76537cc2",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "627a9ae227150692b14be8d780d704fde7a402b8917880ffd0959f14af868a53",
      "created_at": "2026-10-08 02:51:23",
      "finished_at": "2026-10-08 02:51:27",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 3399,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    }
  ]
}
```


For a recorded table/SQL error, inspect the identified table in `database/schema.sql` and the run details. Apply the schema to a local MySQL database following the README to obtain actual database execution results. If no cause or location was captured, it is unknown; missing history is not a pass.
