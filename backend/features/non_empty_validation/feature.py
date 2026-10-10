from flask import Blueprint, request, jsonify
from functools import wraps

blueprint = Blueprint('non_empty_validation', __name__)


def validate_non_empty(field_name='win'):
    """
    Decorator to validate that a specified field in the request JSON is not empty.
    
    Args:
        field_name: The name of the field to validate (default: 'win')
    
    Returns:
        Decorator function that validates the field
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            data = request.get_json(silent=True)
            
            if data is None:
                return jsonify({
                    'error': 'Invalid JSON or no data provided',
                    'field': field_name
                }), 400
            
            if field_name not in data:
                return jsonify({
                    'error': f'{field_name} field is required',
                    'field': field_name
                }), 400
            
            value = data.get(field_name)
            
            # Check if value is None, empty string, or whitespace-only string
            if value is None or (isinstance(value, str) and not value.strip()):
                return jsonify({
                    'error': f'{field_name} input cannot be empty',
                    'field': field_name
                }), 400
            
            return f(*args, **kwargs)
        
        return decorated_function
    return decorator


@blueprint.post('/validate/win')
@validate_non_empty('win')
def validate_win_input():
    """
    Endpoint to validate that the 'win' input is not empty.
    
    Returns:
        JSON response indicating validation success
    """
    data = request.get_json()
    return jsonify({
        'message': 'Validation successful',
        'win': data.get('win')
    }), 200


@blueprint.post('/validate')
@validate_non_empty('win')
def validate_generic():
    """
    Generic validation endpoint for win input.
    
    Returns:
        JSON response with validation result
    """
    data = request.get_json()
    return jsonify({
        'valid': True,
        'data': data
    }), 200
