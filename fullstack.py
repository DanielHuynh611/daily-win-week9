"""Full-stack Flask entry point for local development and EC2 Gunicorn."""
from pathlib import Path

from flask import abort, g, redirect, render_template, send_file

from backend import create_app as create_backend_app
from backend.core.auth import require_auth

PROJECT_ROOT = Path(__file__).resolve().parent
SCREEN_ROUTES = {
    "/": "frontend/features/local_browser_storage/today.html",
    "/history": "frontend/features/local_browser_storage/history.html",
}


def _project_file(relative_path):
    target = (PROJECT_ROOT / relative_path).resolve()
    if PROJECT_ROOT not in target.parents:
        abort(404)
    return target


def create_app(testing=False, config=None):
    app = create_backend_app(testing=testing, config=config)

    @app.get("/static/css/app.css")
    def frontend_css():
        return send_file(_project_file("frontend/shared/ui/library.css"), mimetype="text/css")

    @app.get("/__frontend_assets/<path:relative_path>")
    def frontend_asset(relative_path):
        normalized = relative_path.replace("\\", "/")
        allowed = normalized.startswith("frontend/features/") or normalized in {
            "frontend/shared/ui/library.js", "frontend/shared/ui/runtime.js",
        }
        if not allowed or not normalized.endswith(".js") or ".." in normalized.split("/"):
            abort(404)
        target = _project_file(normalized)
        if not target.is_file():
            abort(404)
        return send_file(target, mimetype="text/javascript")

    for index, (route, relative_path) in enumerate(SCREEN_ROUTES.items()):
        template = relative_path.removeprefix("frontend/")

        @require_auth
        def serve_screen(_template=template):
            return render_template(_template, user=g.user)

        app.add_url_rule(route, endpoint=f"frontend_screen_{index}", view_func=serve_screen)

    # Old generated utility pages are now part of the single Today workflow.
    @app.get("/confirmation")
    @app.get("/internal/timezone-detection")
    @require_auth
    def legacy_screen():
        return redirect("/")
    return app
