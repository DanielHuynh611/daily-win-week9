"""Preserve the generated main-screen API while saving to the account database."""
from flask import Blueprint, jsonify, request
from backend.core.auth import require_auth
from backend.core.wins import create_response, find_win, list_wins, parse_date

blueprint = Blueprint("capability_local_browser_storage_99d93461", __name__)


@blueprint.post("/api/capability_local_browser_storage_99d93461/wins")
@require_auth
def save_win():
    return create_response()


@blueprint.get("/api/capability_local_browser_storage_99d93461/wins")
@require_auth
def get_wins():
    return jsonify(wins=list_wins(request.args.get("date")))


@blueprint.get("/api/capability_local_browser_storage_99d93461/wins/check")
@require_auth
def check_win_exists_for_date():
    day = parse_date(request.args.get("date"))
    win = find_win(day)
    return jsonify(exists=win is not None, date=day.isoformat(), win=win)
