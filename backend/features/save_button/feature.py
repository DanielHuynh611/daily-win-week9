from flask import Blueprint, request, jsonify
from functools import wraps
import jwt
import os
from datetime import datetime

blueprint = Blueprint('save_button', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({'error': 'Invalid token format'}), 401
        
        if not token:
            return jsonify({'error': 'Token is missing'}), 401
        
        try:
            secret_key = os.environ.get('JWT_SECRET_KEY', 'default-secret-key')
            data = jwt.decode(token, secret_key, algorithms=["HS256"])
            request.user_id = data.get('user_id')
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
        
        return f(*args, **kwargs)
    
    return decorated

@blueprint.post('/api/save-win')
@token_required
def save_win():
    """
    Save button endpoint to record a user's win.
    Expects JSON payload with win data.
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        user_id = request.user_id
        timestamp = datetime.utcnow().isoformat()
        
        response = {
            'success': True,
            'message': 'Win recorded successfully',
            'user_id': user_id,
            'timestamp': timestamp,
            'data': data
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@blueprint.get('/api/save-status')
@token_required
def get_save_status():
    """
    Get the current save status for the user.
    """
    try:
        user_id = request.user_id
        
        response = {
            'success': True,
            'user_id': user_id,
            'save_enabled': True
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
