# daily-win full-stack application

This package combines the Backend Generator package unchanged with the
current complete responsive Frontend Generator pages. Each compiled page carries
its visual system locally and does not require a frontend CDN at runtime.

## Run locally

1. Create and activate a Python virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and replace its example values.
4. Connect to the existing MySQL database used by the backend and confirm its
   generated tables are present. Apply `database/schema.sql` once only when
   setting up a new empty database.
5. Run `pytest -q`.
6. Start the complete application:
   `flask --app 'fullstack:create_app()' run --debug`
7. Open a screen route listed in `frontend-package-manifest.json`.

## Understand this codebase

- `fullstack.py` creates the complete Flask app and maps browser URLs to pages.
- `frontend/features/` contains the generated pages and their JavaScript.
- `frontend/shared/` and `frontend/static/` provide shared frontend assets.
- `backend/features/` contains API handlers; `backend/core/` provides shared services.
- `database/schema.sql` defines the MySQL tables the backend uses.
- `tests/` contains generated checks to run locally, not a guarantee of full coverage.

The browser loads a page from Flask. Page actions call the backend API routes;
the handlers use the shared database helpers to read or update MySQL.
Use `frontend-package-manifest.json` to locate screen routes and source snapshots.

## Verification results

Start with [full-stack results](verification/fullstack.md) for commands, captured
output, route conflicts and checks not run. [Frontend results](verification/frontend.md)
contain foundation/screen check history. [VERIFICATION.md](VERIFICATION.md) indexes
the upstream architecture, database and backend reports when present in the source
backend package. Older backend packages may predate these reports.

## Route setup note

Every completed page is included in this package. More than one page requested
the same browser URL, so the runnable starter uses the first page at that URL:

- `/` also has the page `frontend/features/record_daily_achievement/daily_achievement_entry.html`.
- `/` also has the page `frontend/features/one_entry_per_day_limit/daily_win_entry_screen.html`.
- `/` also has the page `frontend/features/save_button/main_entry_screen.html`.
- `/` also has the page `frontend/features/single_screen_interface/main_recording_screen.html`.
- `/` also has the page `frontend/features/non_empty_validation/main_entry_screen_with_validation.html`.
- `/` also has the page `frontend/features/150_character_limit/achievement_entry_screen.html`.
- `/` also has the page `frontend/features/current_date_display/main_entry_screen.html`.
- `/` also has the page `frontend/features/duplicate_entry_prevention/main_entry_screen.html`.
- `/` also has the page `frontend/features/confirmation_message/main_screen_with_confirmation_message.html`.
- `/` also has the page `frontend/features/brief_microcopy/microcopy_display_screen.html`.

Choose a unique URL for each additional page in `fullstack.py` when connecting
the application. If you encounter an error locally, paste it into Goat Helper
for guided debugging.


## Local setup note

The package was assembled successfully, but Zorentia's temporary runtime check
reported:

- `frontend_package_compile_failed`
- `frontend_application_boot_failed`

Your completed files are included. Follow the setup steps above, then paste any
local error into Goat Helper for guided debugging.

