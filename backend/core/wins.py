"""One account-owned store used by all of the generated win endpoints."""
import uuid
from datetime import date, datetime, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from flask import g, jsonify, request
from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError

from backend.core.db import get_engine, wins


class InputError(ValueError):
    pass


def body():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        raise InputError("Request body must be a JSON object.")
    return payload


def parse_date(value):
    if not isinstance(value, str) or len(value) != 10:
        raise InputError("Date must be in YYYY-MM-DD format.")
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise InputError("Date must be in YYYY-MM-DD format.") from error


def current_local_date():
    name = request.headers.get("X-Time-Zone", "UTC")
    if len(name) > 64:
        raise InputError("Choose a valid device time zone.")
    try:
        zone = ZoneInfo(name)
    except (ZoneInfoNotFoundError, ValueError) as error:
        raise InputError("Choose a valid device time zone.") from error
    return datetime.now(zone).date(), name


def serialize(row):
    created = row["created_at"].replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")
    return {
        "id": row["id"], "achievement_text": row["achievement_text"],
        "date": row["date"].isoformat(), "created_at": created,
    }


def find_win(entry_date):
    day = parse_date(entry_date) if isinstance(entry_date, str) else entry_date
    with get_engine().connect() as connection:
        row = connection.execute(select(wins).where(
            wins.c.user_id == g.user["id"], wins.c.date == day,
        )).mappings().first()
    return serialize(row) if row else None


def list_wins(day=None):
    query = select(wins).where(wins.c.user_id == g.user["id"])
    if day is not None:
        query = query.where(wins.c.date == parse_date(day))
    with get_engine().connect() as connection:
        return [serialize(row) for row in connection.execute(
            query.order_by(wins.c.date.desc(), wins.c.created_at.desc())
        ).mappings()]


def save_win(payload):
    achievement = payload.get("achievement_text", payload.get("text"))
    if not isinstance(achievement, str) or not 1 <= len(achievement.strip()) <= 150:
        raise InputError("Achievement text must be between 1 and 150 characters.")
    today, zone = current_local_date()
    day = parse_date(payload.get("date", payload.get("entry_date", today.isoformat())))
    if day != today:
        raise InputError("Only today's win can be recorded. Refresh the page for the current date.")
    record = {
        "id": str(uuid.uuid4()), "user_id": g.user["id"], "date": day,
        "achievement_text": achievement.strip(), "timezone": zone,
        "created_at": datetime.now(timezone.utc).replace(tzinfo=None),
    }
    try:
        with get_engine().begin() as connection:
            connection.execute(insert(wins).values(**record))
    except IntegrityError:
        # The unique account/day constraint also protects simultaneous submissions.
        if find_win(day):
            return jsonify(
                error="ENTRY_ALREADY_EXISTS",
                message="Today's win is already recorded. Come back tomorrow.",
            ), 409
        raise
    return serialize(record)


def create_response(style="win"):
    result = save_win(body())
    if not isinstance(result, dict):
        return result
    if style == "achievement":
        result = dict(result, recorded_date=result["date"])
        return jsonify(success=True, achievement=result), 201
    if style == "entry":
        return jsonify(dict(result, entry_date=result["date"])), 201
    if style == "duplicate":
        return jsonify(success=True, win=dict(result, entry_date=result["date"])), 201
    if style == "text":
        return jsonify(dict(result, text=result["achievement_text"])), 201
    return jsonify(result), 201
