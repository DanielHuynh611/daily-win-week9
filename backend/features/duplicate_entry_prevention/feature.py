"""Duplicate prevention delegates to the shared database uniqueness constraint."""
from flask import Blueprint, jsonify, request
from backend.core.auth import require_auth
from backend.core.wins import create_response, current_local_date, find_win, parse_date

blueprint = Blueprint("capability_duplicate_entry_prevention_00baa1bc", __name__)


@blueprint.get("/api/capability_duplicate_entry_prevention_00baa1bc/wins/check")
@blueprint.get("/api/capability_duplicate_entry_prevention_00baa1bc/wins/check-today")
@require_auth
def check_today_win_exists():
    today, _zone = current_local_date()
    win = find_win(parse_date(request.args.get("date", today.isoformat())))
    if win:
        win["entry_date"] = win["date"]
    return jsonify(exists=win is not None, entry=win)


@blueprint.post("/api/capability_duplicate_entry_prevention_00baa1bc/wins")
@require_auth
def create_win_with_duplicate_check():
    return create_response("duplicate")
