"""The original interface copy requires no mutable administration API or table."""
from flask import Blueprint, jsonify

blueprint = Blueprint("capability_brief_microcopy_76537cc2", __name__)
MICROCOPY = {
    "input_prompt": "What is one win from today?",
    "success_message": "Today's win saved!",
    "duplicate_entry_message": "Today's win is already recorded. Come back tomorrow.",
    "general_error_message": "Something went wrong. Please try again.",
}


@blueprint.get("/api/capability_brief_microcopy_76537cc2/microcopy")
def get_microcopy_strings():
    return jsonify(microcopy=MICROCOPY)
