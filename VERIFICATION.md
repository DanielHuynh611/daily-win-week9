# Verification results

## Repaired Week 9 application (10 October 2026)

- 50 automated checks passed, including auth, ownership, validation and restart persistence.
- The MySQL schema and Flask CLI commands were checked against an isolated MySQL server.
- Concurrent same-account submissions returned one 201 and one 409, with one stored record.
- Desktop and mobile browser checks passed for registration, saving, refresh, login/logout,
  account isolation, sidebar navigation and confirmation, with no JavaScript errors.
- The original generated CSS and all original sidebar links were preserved.
- Gunicorn started successfully using `fullstack:create_app()`.
- AWS configuration is provided in `deploy/`; deployment on EC2 remains to be performed.

## Original Zorentia generation reports

The reports and package manifests below describe the original downloaded package.
Their generation failures are retained as historical evidence, not current runtime results.

Start with the report for the part of the application you are working on:

- [Architecture](verification/architecture.md): contracts, coverage and retained validation attempts.
- [Database](verification/database.md): SQL generation, recorded failures and execution limits.
- [Backend](verification/backend.md): static checks, affected files and generation/repair history.
- For a full-stack download, open `verification/frontend.md` and `verification/fullstack.md`
  (linked directly in `README-FULLSTACK.md`). They contain frontend checks, route conflicts,
  commands, exit codes and captured output.

Reports describe this package's snapshots. They do not update after you edit the files.
Passed checks only cover their stated scope. Historical failed attempts are distinguished
from current findings. Missing evidence and checks not run are stated explicitly.
Reports do not certify production readiness or complete business functionality.
