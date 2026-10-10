from flask import Blueprint, jsonify, request
from datetime import datetime

blueprint = Blueprint('confirmation_message', __name__)

@blueprint.post('/api/confirmation')
def show_confirmation():
    """
    Display a confirmation message with today's date after saving an entry.
    
    Expected request body:
    {
        "message": "Entry saved successfully" (optional)
    }
    
    Returns:
    {
        "success": true,
        "confirmation": "Entry saved successfully",
        "date": "2024-01-15",
        "timestamp": "2024-01-15T10:30:00"
    }
    """
    data = request.get_json() or {}
    
    default_message = "Entry saved successfully"
    confirmation_message = data.get('message', default_message)
    
    today = datetime.now()
    
    response = {
        "success": True,
        "confirmation": confirmation_message,
        "date": today.strftime("%Y-%m-%d"),
        "timestamp": today.isoformat()
    }
    
    return jsonify(response), 200


@blueprint.get('/api/confirmation/format')
def get_confirmation_format():
    """
    Get the expected format for confirmation messages.
    
    Returns:
    {
        "format": {
            "success": "boolean",
            "confirmation": "string",
            "date": "YYYY-MM-DD",
            "timestamp": "ISO 8601 format"
        },
        "example": {
            "success": true,
            "confirmation": "Entry saved successfully",
            "date": "2024-01-15",
            "timestamp": "2024-01-15T10:30:00"
        }
    }
    """
    response = {
        "format": {
            "success": "boolean",
            "confirmation": "string",
            "date": "YYYY-MM-DD",
            "timestamp": "ISO 8601 format"
        },
        "example": {
            "success": True,
            "confirmation": "Entry saved successfully",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "timestamp": datetime.now().isoformat()
        }
    }
    
    return jsonify(response), 200
