"""Length validation and achievement aliases for the original generated screens."""
from flask import Blueprint, jsonify
from backend.core.auth import require_auth
from backend.core.wins import InputError, body, create_response, find_win

blueprint = Blueprint("capability_150_character_limit_2a9520cb", __name__)


@blueprint.post("/api/capability_150_character_limit_2a9520cb/achievements/validate")
@require_auth
def validate_achievement_text():
    value = body().get("text")
    if not isinstance(value, str):
        raise InputError("Achievement text is required.")
    valid = 1 <= len(value.strip()) <= 150
    result = {"valid": valid, "character_count": len(value)}
    if not valid:
        result["error_message"] = "Achievement text must be between 1 and 150 characters."
    return jsonify(result)


@blueprint.post("/api/capability_150_character_limit_2a9520cb/achievements")
@require_auth
def create_achievement():
    return create_response("text")


@blueprint.get("/api/capability_150_character_limit_2a9520cb/achievements/<date>")
@require_auth
def get_achievement_by_date(date):
    win = find_win(date)
    if not win:
        return jsonify(error="NOT_FOUND", message="No achievement found for this date."), 404
    return jsonify(dict(win, text=win["achievement_text"]))
