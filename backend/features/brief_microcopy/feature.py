"""
Brief microcopy feature module.

Provides microcopy strings for prompts, confirmations, and error messages
throughout the user interface.
"""

from flask import Blueprint, jsonify, request, g
from sqlalchemy import text
from functools import wraps
import uuid

blueprint = Blueprint('capability_brief_microcopy_76537cc2', __name__)


def get_db():
    """Get database connection from Flask g object."""
    from flask import current_app
    if 'db' not in g:
        g.db = current_app.config['DATABASE_ENGINE']
    return g.db


def require_auth(f):
    """Decorator for routes requiring authentication."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check for authentication token or session
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function


@blueprint.route('/api/capability_brief_microcopy_76537cc2/microcopy', methods=['GET'])
def get_microcopy_strings():
    """
    Retrieves all active microcopy strings to display prompts, confirmations,
    and error messages throughout the user interface.
    
    Returns:
        JSON response with microcopy strings or error message
    """
    try:
        db = get_db()
        
        query = text("""
            SELECT `key`, `text_content`
            FROM `f_76537cc2__microcopy_strings`
            WHERE `is_active` = 1
        """)
        
        with db.connect() as conn:
            result = conn.execute(query)
            rows = result.fetchall()
        
        # Build microcopy dictionary from database results
        microcopy_dict = {}
        for row in rows:
            key = row[0]
            text_content = row[1]
            microcopy_dict[key] = text_content
        
        # Ensure all required keys are present
        required_keys = [
            'input_prompt',
            'success_message',
            'duplicate_entry_message',
            'general_error_message'
        ]
        
        for key in required_keys:
            if key not in microcopy_dict:
                microcopy_dict[key] = ''
        
        return jsonify({
            'microcopy': {
                'input_prompt': microcopy_dict.get('input_prompt', ''),
                'success_message': microcopy_dict.get('success_message', ''),
                'duplicate_entry_message': microcopy_dict.get('duplicate_entry_message', ''),
                'general_error_message': microcopy_dict.get('general_error_message', '')
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Unable to load interface text'}), 500


@blueprint.route('/api/admin/microcopy/initialize', methods=['POST'])
@require_auth
def initialize_microcopy_strings():
    """
    Creates the initial set of microcopy strings with the exact wording
    specified in acceptance criteria during application setup.
    
    Returns:
        JSON response indicating success or error
    """
    try:
        db = get_db()
        
        # Check if microcopy strings already exist
        check_query = text("""
            SELECT COUNT(*) as count
            FROM `f_76537cc2__microcopy_strings`
        """)
        
        with db.connect() as conn:
            result = conn.execute(check_query)
            row = result.fetchone()
            count = row[0]
        
        if count > 0:
            return jsonify({'error': 'Microcopy strings already initialized'}), 409
        
        # Define the initial microcopy strings based on acceptance criteria
        microcopy_strings = [
            {
                'id': str(uuid.uuid4()),
                'key': 'input_prompt',
                'text_content': 'What is one win from today?',
                'context': 'Input field prompt for daily win entry',
                'is_active': 1
            },
            {
                'id': str(uuid.uuid4()),
                'key': 'success_message',
                'text_content': "Today's win saved!",
                'context': 'Confirmation message after successfully saving a win',
                'is_active': 1
            },
            {
                'id': str(uuid.uuid4()),
                'key': 'duplicate_entry_message',
                'text_content': "Today's win is already recorded",
                'context': 'Message when user attempts to save a second win on the same day',
                'is_active': 1
            },
            {
                'id': str(uuid.uuid4()),
                'key': 'general_error_message',
                'text_content': 'Something went wrong. Please try again.',
                'context': 'Clear, supportive error message for general errors',
                'is_active': 1
            }
        ]
        
        # Insert microcopy strings into database
        insert_query = text("""
            INSERT INTO `f_76537cc2__microcopy_strings`
            (`id`, `key`, `text_content`, `context`, `is_active`)
            VALUES (:id, :key, :text_content, :context, :is_active)
        """)
        
        with db.connect() as conn:
            for microcopy in microcopy_strings:
                conn.execute(insert_query, microcopy)
            conn.commit()
        
        return jsonify({
            'initialized': True,
            'count': len(microcopy_strings)
        }), 200
        
    except Exception as e:
        return jsonify({'error': 'Failed to initialize microcopy strings'}), 500
