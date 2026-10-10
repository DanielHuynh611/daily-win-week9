from flask import Blueprint, jsonify
from datetime import datetime

blueprint = Blueprint('current_date_display', __name__)

@blueprint.get('/api/current-date')
def get_current_date():
    """
    Returns the current calendar date to the user.
    
    Returns:
        JSON response containing the current date in ISO format
    """
    try:
        current_date = datetime.now().date()
        return jsonify({
            'success': True,
            'date': current_date.isoformat(),
            'formatted_date': current_date.strftime('%B %d, %Y'),
            'day': current_date.day,
            'month': current_date.month,
            'year': current_date.year,
            'day_of_week': current_date.strftime('%A')
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Failed to retrieve current date',
            'message': str(e)
        }), 500
