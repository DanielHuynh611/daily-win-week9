"""Record achievements using the shared authenticated win store."""
from flask import Blueprint, jsonify
from backend.core.auth import require_auth
from backend.core.wins import create_response, current_local_date, find_win

blueprint = Blueprint("capability_record_daily_achievement_86a57805", __name__)


@blueprint.get("/api/capability_record_daily_achievement_86a57805/achievements/today")
@require_auth
def check_today_entry():
    today, _zone = current_local_date()
    achievement = find_win(today)
    if achievement:
        achievement["recorded_date"] = achievement["date"]
    return jsonify(exists=achievement is not None, achievement=achievement)


@blueprint.post("/api/capability_record_daily_achievement_86a57805/achievements")
@require_auth
def save_achievement():
    return create_response("achievement")
