# Full-stack verification

These checks use a temporary directory and verification configuration, not your deployment. The smoke command requests registered pages and JavaScript assets; it does not exercise form submissions or database business operations.

## Findings and next steps

```json
{
  "finding": "frontend_package_compile_failed"
}
```

Expected parseable Python; the syntax/compile check did not pass. Inspect the reported file and line, correct the syntax, then rerun the recorded command.

```json
{
  "finding": "frontend_application_boot_failed"
}
```

Expected imports/application startup to succeed. Use the traceback below to locate the failing module, dependency or configuration, then rerun the same command locally.

## Static assembly evidence
```json
{
  "static_valid": true,
  "backend_package_reused_unchanged": true,
  "route_collisions_absent": false,
  "route_collisions": [
    {
      "route": "/",
      "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
      "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
      "unregistered_screen_id": "capability_record_daily_achievement_86a57805.screen.main",
      "unregistered_path": "frontend/features/record_daily_achievement/daily_achievement_entry.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
      "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
      "unregistered_screen_id": "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry",
      "unregistered_path": "frontend/features/one_entry_per_day_limit/daily_win_entry_screen.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
      "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
      "unregistered_screen_id": "capability_save_button_5553765f.screen.main_entry",
      "unregistered_path": "frontend/features/save_button/main_entry_screen.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
      "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
      "unregistered_screen_id": "capability_single_screen_interface_20b1b421.screen.main",
      "unregistered_path": "frontend/features/single_screen_interface/main_recording_screen.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
      "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
      "unregistered_screen_id": "capability_non_empty_validation_c7515c58.screen.main_entry",
      "unregistered_path": "frontend/features/non_empty_validation/main_entry_screen_with_validation.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
      "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
      "unregistered_screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
      "unregistered_path": "frontend/features/150_character_limit/achievement_entry_screen.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
      "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
      "unregistered_screen_id": "capability_current_date_display_67c458ab.screen.main_entry",
      "unregistered_path": "frontend/features/current_date_display/main_entry_screen.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
      "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
      "unregistered_screen_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
      "unregistered_path": "frontend/features/duplicate_entry_prevention/main_entry_screen.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
      "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
      "unregistered_screen_id": "capability_confirmation_message_23ce028f.screen.main_with_confirmation",
      "unregistered_path": "frontend/features/confirmation_message/main_screen_with_confirmation_message.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
      "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
      "unregistered_screen_id": "capability_brief_microcopy_76537cc2.screen.microcopy_display",
      "unregistered_path": "frontend/features/brief_microcopy/microcopy_display_screen.html"
    }
  ],
  "screen_files_present": true,
  "self_contained_frontend": true,
  "legacy_runtime_normalized_paths": [],
  "source_snapshot_hash": "348616e7a59478c304100a6e839a728875a95f7c31612ca466c560d3329d3d1a",
  "errors": []
}
```

## Routes needing attention
The first page registered at a URL is served; additional pages remain in the ZIP. Choose unique routes for the unregistered paths in `fullstack.py`, update page links and rerun the route smoke check.
```json
[
  {
    "route": "/",
    "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
    "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
    "unregistered_screen_id": "capability_record_daily_achievement_86a57805.screen.main",
    "unregistered_path": "frontend/features/record_daily_achievement/daily_achievement_entry.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
    "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
    "unregistered_screen_id": "capability_one_entry_per_day_limit_86f08838.screen.daily_win_entry",
    "unregistered_path": "frontend/features/one_entry_per_day_limit/daily_win_entry_screen.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
    "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
    "unregistered_screen_id": "capability_save_button_5553765f.screen.main_entry",
    "unregistered_path": "frontend/features/save_button/main_entry_screen.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
    "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
    "unregistered_screen_id": "capability_single_screen_interface_20b1b421.screen.main",
    "unregistered_path": "frontend/features/single_screen_interface/main_recording_screen.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
    "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
    "unregistered_screen_id": "capability_non_empty_validation_c7515c58.screen.main_entry",
    "unregistered_path": "frontend/features/non_empty_validation/main_entry_screen_with_validation.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
    "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
    "unregistered_screen_id": "capability_150_character_limit_2a9520cb.screen.achievement_entry",
    "unregistered_path": "frontend/features/150_character_limit/achievement_entry_screen.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
    "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
    "unregistered_screen_id": "capability_current_date_display_67c458ab.screen.main_entry",
    "unregistered_path": "frontend/features/current_date_display/main_entry_screen.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
    "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
    "unregistered_screen_id": "capability_duplicate_entry_prevention_00baa1bc.screen.main_entry",
    "unregistered_path": "frontend/features/duplicate_entry_prevention/main_entry_screen.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
    "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
    "unregistered_screen_id": "capability_confirmation_message_23ce028f.screen.main_with_confirmation",
    "unregistered_path": "frontend/features/confirmation_message/main_screen_with_confirmation_message.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_local_browser_storage_99d93461.screen.main",
    "registered_path": "frontend/features/local_browser_storage/main_win_entry_screen.html",
    "unregistered_screen_id": "capability_brief_microcopy_76537cc2.screen.microcopy_display",
    "unregistered_path": "frontend/features/brief_microcopy/microcopy_display_screen.html"
  }
]
```

## Runtime commands and captured results
```json
{
  "valid": false,
  "passes": {
    "compile": false,
    "application_start": false,
    "screen_routes": false,
    "self_contained_frontend": false,
    "frontend_assets": false
  },
  "commands": [
    {
      "command": [
        "/home/ubuntu/zorentia-app/venv/bin/python",
        "-m",
        "compileall",
        "-q",
        "backend",
        "frontend",
        "fullstack.py"
      ],
      "returncode": 1,
      "stdout": "*** Error compiling 'backend/app.py'...\n  File \"backend/app.py\", line 11\n    from backend.features.150_character_limit.feature import blueprint as 150_character_limit_blueprint\n                             ^\nSyntaxError: invalid decimal literal\n\n",
      "stderr": "",
      "timed_out": false
    },
    {
      "command": [
        "/home/ubuntu/zorentia-app/venv/bin/python",
        "-c",
        "from fullstack import create_app;app=create_app(testing=True);client=app.test_client();routes=['/', '/internal/timezone-detection', '/confirmation'];responses=[client.get(route) for route in routes];print({'route_checks':[{'route':route,'status':response.status_code,'html_doctype':b'<!doctype html' in response.data.lower(),'compiler_marker':b'data-zorentia-compiler' in response.data} for route,response in zip(routes,responses)]},flush=True);assert responses and all(response.status_code==200 for response in responses);assert all(b'<!doctype html' in response.data.lower() for response in responses);assert all(b'data-zorentia-compiler' in response.data for response in responses);assets=['/__frontend_assets/frontend/shared/ui/library.js', '/__frontend_assets/frontend/shared/ui/runtime.js', '/__frontend_assets/frontend/features/local_browser_storage/main_win_entry_screen.js', '/__frontend_assets/frontend/features/device_timezone_detection/timezone_detection_service.js', '/__frontend_assets/frontend/features/record_daily_achievement/daily_achievement_entry.js', '/__frontend_assets/frontend/features/one_entry_per_day_limit/daily_win_entry_screen.js', '/__frontend_assets/frontend/features/save_button/main_entry_screen.js', '/__frontend_assets/frontend/features/single_screen_interface/main_recording_screen.js', '/__frontend_assets/frontend/features/non_empty_validation/main_entry_screen_with_validation.js', '/__frontend_assets/frontend/features/150_character_limit/achievement_confirmation_screen.js', '/__frontend_assets/frontend/features/150_character_limit/achievement_entry_screen.js', '/__frontend_assets/frontend/features/current_date_display/main_entry_screen.js', '/__frontend_assets/frontend/features/duplicate_entry_prevention/main_entry_screen.js', '/__frontend_assets/frontend/features/confirmation_message/main_screen_with_confirmation_message.js', '/__frontend_assets/frontend/features/brief_microcopy/microcopy_display_screen.js'];asset_responses=[client.get(asset) for asset in assets];print({'asset_checks':[{'path':asset,'status':response.status_code,'content_type':response.content_type} for asset,response in zip(assets,asset_responses)]},flush=True);assert all(response.status_code==200 for response in asset_responses);assert all('javascript' in response.content_type for response in asset_responses);print({'routes':[(route,response.status_code) for route,response in zip(routes,responses)],'assets':[(asset,response.status_code) for asset,response in zip(assets,asset_responses)]})"
      ],
      "returncode": 1,
      "stdout": "",
      "stderr": "Traceback (most recent call last):\n  File \"<string>\", line 1, in <module>\n  File \"/tmp/zorentia-frontend-verify-bpg50i9f/fullstack.py\", line 7, in <module>\n    from backend import create_app as create_backend_app\n  File \"/tmp/zorentia-frontend-verify-bpg50i9f/backend/__init__.py\", line 1, in <module>\n    from .app import create_app\n  File \"/tmp/zorentia-frontend-verify-bpg50i9f/backend/app.py\", line 11\n    from backend.features.150_character_limit.feature import blueprint as 150_character_limit_blueprint\n                             ^\nSyntaxError: invalid decimal literal\n",
      "timed_out": false
    }
  ],
  "errors": [
    "frontend_package_compile_failed",
    "frontend_application_boot_failed"
  ],
  "execution_scope": {
    "compile": "executed",
    "application_start_and_route_asset_smoke": "executed",
    "not_run": [
      "MySQL schema execution",
      "pytest",
      "browser interaction",
      "end-to-end business behavior",
      "deployment verification"
    ],
    "output_limit": "Each command retains the last 8000 characters of stdout/stderr; earlier output may be unavailable."
  }
}
```

Reproduce a failure using the recorded command from the package root after following README-FULLSTACK.md. For the smoke command, use your environment's Python executable. Compare the traceback, file/line and exit code; a timeout does not establish a code defect.
