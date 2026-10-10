"""Use the browser's IANA time zone and the same owned win records."""
from flask import Blueprint, g, jsonify
from sqlalchemy import select

from backend.core.auth import require_auth
from backend.core.db import get_engine, wins
from backend.core.wins import InputError, body, current_local_date, find_win, parse_date

blueprint = Blueprint("capability_device_timezone_detection_aca07cc7", __name__)


@blueprint.get("/api/capability_device_timezone_detection_aca07cc7/local-date/current")
@require_auth
def get_current_local_date():
    today, zone = current_local_date()
    return jsonify(local_date=today.isoformat(), timezone=zone)


@blueprint.post("/api/capability_device_timezone_detection_aca07cc7/local-date/check")
@require_auth
def check_entry_exists_for_date():
    win = find_win(parse_date(body().get("local_date")))
    return jsonify(exists=win is not None, entry_id=win["id"] if win else None)


@blueprint.post("/api/capability_device_timezone_detection_aca07cc7/local-date/record")
@require_auth
def record_entry_local_date():
    payload = body()
    day = parse_date(payload.get("local_date"))
    entry_id = payload.get("entry_id")
    if not isinstance(entry_id, str):
        raise InputError("A saved entry ID is required.")
    with get_engine().connect() as connection:
        record = connection.execute(select(wins).where(
            wins.c.id == entry_id, wins.c.user_id == g.user["id"], wins.c.date == day,
        )).mappings().first()
    if not record:
        return jsonify(error="NOT_FOUND", message="No matching saved win was found."), 404
    return jsonify(
        id=record["id"], entry_id=record["id"], local_date=day.isoformat(),
        created_at_utc=record["created_at"].isoformat() + "Z",
    )
