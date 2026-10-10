"""
Local browser storage feature module for managing win entries.
"""
from flask import Blueprint, request, jsonify
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import uuid
import re

blueprint = Blueprint('capability_local_browser_storage_99d93461', __name__)


def get_db_connection():
    """Get database connection from Flask app context."""
    from flask import current_app
    return current_app.config['db_engine'].connect()


def validate_date_format(date_string):
    """Validate date string is in YYYY-MM-DD format."""
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(pattern, date_string):
        return False
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


@blueprint.post('/api/capability_local_browser_storage_99d93461/wins')
def save_win():
    """
    Save a new win entry to the database.
    Validates achievement text length and one-entry-per-day constraint.
    """
    data = request.get_json()
    
    if not data:
        return jsonify({
            'error': 'INVALID_REQUEST',
            'message': 'Request body must be JSON'
        }), 400
    
    achievement_text = data.get('achievement_text')
    date = data.get('date')
    
    # Validate required fields
    if not achievement_text:
        return jsonify({
            'error': 'INVALID_ACHIEVEMENT_TEXT',
            'message': 'Achievement text must be between 1 and 150 characters'
        }), 400
    
    if not date:
        return jsonify({
            'error': 'INVALID_DATE',
            'message': 'Date must be provided in YYYY-MM-DD format'
        }), 400
    
    # Validate achievement text length
    if not isinstance(achievement_text, str) or len(achievement_text) < 1 or len(achievement_text) > 150:
        return jsonify({
            'error': 'INVALID_ACHIEVEMENT_TEXT',
            'message': 'Achievement text must be between 1 and 150 characters'
        }), 400
    
    # Validate date format
    if not validate_date_format(date):
        return jsonify({
            'error': 'INVALID_DATE',
            'message': 'Date must be provided in YYYY-MM-DD format'
        }), 400
    
    # Check if entry already exists for this date
    conn = get_db_connection()
    try:
        check_query = text("""
            SELECT id FROM f_99d93461__wins WHERE date = :date
        """)
        result = conn.execute(check_query, {'date': date})
        existing = result.fetchone()
        
        if existing:
            return jsonify({
                'error': 'ENTRY_ALREADY_EXISTS',
                'message': 'A win has already been recorded for this date'
            }), 409
        
        # Generate UUID and timestamp
        win_id = str(uuid.uuid4())
        created_at = datetime.utcnow()
        
        # Insert new win
        insert_query = text("""
            INSERT INTO f_99d93461__wins (id, date, achievement_text, created_at)
            VALUES (:id, :date, :achievement_text, :created_at)
        """)
        
        conn.execute(insert_query, {
            'id': win_id,
            'date': date,
            'achievement_text': achievement_text,
            'created_at': created_at
        })
        conn.commit()
        
        return jsonify({
            'id': win_id,
            'achievement_text': achievement_text,
            'date': date,
            'created_at': created_at.isoformat() + 'Z'
        }), 201
        
    except Exception as e:
        conn.rollback()
        raise
    finally:
        conn.close()


@blueprint.get('/api/capability_local_browser_storage_99d93461/wins')
def get_wins():
    """
    Retrieve all win entries, optionally filtered by date.
    """
    date_filter = request.args.get('date')
    
    # Validate date filter if provided
    if date_filter:
        if not validate_date_format(date_filter):
            return jsonify({
                'error': 'INVALID_DATE_FILTER',
                'message': 'Date filter must be in YYYY-MM-DD format'
            }), 400
    
    conn = get_db_connection()
    try:
        if date_filter:
            query = text("""
                SELECT id, date, achievement_text, created_at
                FROM f_99d93461__wins
                WHERE date = :date
                ORDER BY created_at DESC
            """)
            result = conn.execute(query, {'date': date_filter})
        else:
            query = text("""
                SELECT id, date, achievement_text, created_at
                FROM f_99d93461__wins
                ORDER BY created_at DESC
            """)
            result = conn.execute(query)
        
        wins = []
        for row in result:
            wins.append({
                'id': row[0],
                'date': row[1].isoformat() if hasattr(row[1], 'isoformat') else str(row[1]),
                'achievement_text': row[2],
                'created_at': row[3].isoformat() + 'Z' if hasattr(row[3], 'isoformat') else str(row[3])
            })
        
        return jsonify({
            'wins': wins
        }), 200
        
    finally:
        conn.close()


@blueprint.get('/api/capability_local_browser_storage_99d93461/wins/check')
def check_win_exists_for_date():
    """
    Check if a win entry exists for a specific date.
    """
    date = request.args.get('date')
    
    if not date:
        return jsonify({
            'error': 'INVALID_DATE',
            'message': 'Date must be provided in YYYY-MM-DD format'
        }), 400
    
    # Validate date format
    if not validate_date_format(date):
        return jsonify({
            'error': 'INVALID_DATE',
            'message': 'Date must be provided in YYYY-MM-DD format'
        }), 400
    
    conn = get_db_connection()
    try:
        query = text("""
            SELECT id, achievement_text, created_at
            FROM f_99d93461__wins
            WHERE date = :date
        """)
        result = conn.execute(query, {'date': date})
        row = result.fetchone()
        
        if row:
            return jsonify({
                'exists': True,
                'date': date,
                'win': {
                    'id': row[0],
                    'achievement_text': row[1],
                    'created_at': row[2].isoformat() + 'Z' if hasattr(row[2], 'isoformat') else str(row[2])
                }
            }), 200
        else:
            return jsonify({
                'exists': False,
                'date': date
            }), 200
        
    finally:
        conn.close()
