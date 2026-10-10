"""
Flask module implementing 150 character limit capability for achievements.
"""
import uuid
from datetime import datetime
from flask import Blueprint, request, jsonify
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from db import get_db

blueprint = Blueprint('capability_150_character_limit_2a9520cb', __name__)


@blueprint.post('/api/capability_150_character_limit_2a9520cb/achievements/validate')
def validate_achievement_text():
    """
    Validates that achievement text does not exceed 150 characters before allowing save operation.
    """
    data = request.get_json()
    
    if data is None or 'text' not in data:
        return jsonify({'error': 'Invalid request: text field is required'}), 400
    
    text = data.get('text')
    
    if text is None:
        return jsonify({'error': 'Invalid request: text field is required'}), 400
    
    character_count = len(text)
    valid = character_count <= 150
    
    response = {
        'valid': valid,
        'character_count': character_count
    }
    
    if not valid:
        response['error_message'] = f'Text exceeds the maximum allowed length of 150 characters (current: {character_count})'
    
    return jsonify(response), 200


@blueprint.post('/api/capability_150_character_limit_2a9520cb/achievements')
def create_achievement():
    """
    Creates a new achievement entry after enforcing the 150 character limit on the text field.
    """
    data = request.get_json()
    
    if data is None:
        return jsonify({'error': 'Achievement text is required and must be at least 1 character'}), 400
    
    text = data.get('text')
    date_str = data.get('date')
    
    # Validate text presence
    if not text or len(text) == 0:
        return jsonify({'error': 'Achievement text is required and must be at least 1 character'}), 400
    
    # Validate text length
    if len(text) > 150:
        return jsonify({
            'error': 'Achievement text must not exceed 150 characters',
            'character_count': len(text),
            'maximum_allowed': 150
        }), 400
    
    # Validate date presence and format
    if not date_str:
        return jsonify({'error': 'Valid date is required in YYYY-MM-DD format'}), 400
    
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except (ValueError, TypeError):
        return jsonify({'error': 'Valid date is required in YYYY-MM-DD format'}), 400
    
    db = get_db()
    
    # Check if achievement already exists for this date
    check_query = text("""
        SELECT id FROM f_2a9520cb__achievements WHERE date = :date
    """)
    
    existing = db.execute(check_query, {'date': date_str}).fetchone()
    
    if existing:
        return jsonify({'error': 'An achievement has already been recorded for this date'}), 409
    
    # Create new achievement
    achievement_id = str(uuid.uuid4())
    created_at = datetime.utcnow()
    
    insert_query = text("""
        INSERT INTO f_2a9520cb__achievements (id, text, date, created_at)
        VALUES (:id, :text, :date, :created_at)
    """)
    
    try:
        db.execute(insert_query, {
            'id': achievement_id,
            'text': text,
            'date': date_str,
            'created_at': created_at
        })
        db.commit()
    except IntegrityError:
        db.rollback()
        return jsonify({'error': 'An achievement has already been recorded for this date'}), 409
    except Exception as e:
        db.rollback()
        return jsonify({'error': 'Failed to create achievement'}), 500
    
    return jsonify({
        'id': achievement_id,
        'text': text,
        'date': date_str,
        'created_at': created_at.isoformat() + 'Z'
    }), 201


@blueprint.get('/api/capability_150_character_limit_2a9520cb/achievements/<date>')
def get_achievement_by_date(date):
    """
    Retrieves an existing achievement for a specific date.
    """
    # Validate date format
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except (ValueError, TypeError):
        return jsonify({'error': 'Valid date is required in YYYY-MM-DD format'}), 400
    
    db = get_db()
    
    query = text("""
        SELECT id, text, date, created_at
        FROM f_2a9520cb__achievements
        WHERE date = :date
    """)
    
    result = db.execute(query, {'date': date}).fetchone()
    
    if not result:
        return jsonify({'error': 'No achievement found for the specified date'}), 404
    
    return jsonify({
        'id': result[0],
        'text': result[1],
        'date': result[2].isoformat() if hasattr(result[2], 'isoformat') else str(result[2]),
        'created_at': result[3].isoformat() + 'Z' if hasattr(result[3], 'isoformat') else str(result[3])
    }), 200
