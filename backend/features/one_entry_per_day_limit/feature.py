"""All feature aliases enforce one win per account and calendar day."""
from flask import Blueprint, jsonify, request
from backend.core.auth import require_auth
from backend.core.wins import create_response, find_win, parse_date

blueprint = Blueprint("capability_one_entry_per_day_limit_86f08838", __name__)


@blueprint.get("/api/capability_one_entry_per_day_limit_86f08838/daily-wins/check")
@require_auth
def check_entry_exists_for_date():
    day = parse_date(request.args.get("entry_date"))
    return jsonify(exists=find_win(day) is not None, entry_date=day.isoformat())


@blueprint.post("/api/capability_one_entry_per_day_limit_86f08838/daily-wins")
@require_auth
def create_daily_win_entry():
    return create_response("entry")


@blueprint.get("/api/capability_one_entry_per_day_limit_86f08838/daily-wins/<entry_date>")
@require_auth
def get_entry_for_date(entry_date):
    win = find_win(entry_date)
    if not win:
        return jsonify(error="ENTRY_NOT_FOUND", message="No win entry exists for this date."), 404
    return jsonify(dict(win, entry_date=win["date"]))
