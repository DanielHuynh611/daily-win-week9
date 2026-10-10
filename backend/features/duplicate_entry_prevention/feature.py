"""
Duplicate entry prevention feature module.

This module prevents users from adding multiple win entries for the same day.
"""

from flask import Blueprint, request, jsonify
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import uuid

# Assuming db is imported from the application factory or a shared module
# In a real application, this would be: from app import db
# For this module, we'll assume db is injected or available
from extensions import db

blueprint = Blueprint('capability_duplicate_entry_prevention_00baa1bc', __name__)


def validate_date_format(date_string):
    """Validate that the date string is in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except (ValueError, TypeError):
        return False


def validate_achievement_text(text):
    """Validate that achievement text is between 1 and 150 characters."""
    if not text or not isinstance(text, str):
        return False
    return 1 <= len(text) <= 150


@blueprint.get('/api/capability_duplicate_entry_prevention_00baa1bc/wins/check-today')
def check_today_win_exists():
    """
    Checks if a win entry already exists for the current date to enable 
    duplicate prevention logic in the UI.
    
    Query Parameters:
        date: The date to check in YYYY-MM-DD format
        
    Returns:
        JSON response with exists flag and optional entry data
    """
    date_param = request.args.get('date')
    
    if not date_param:
        return jsonify({
            'error': 'INVALID_DATE',
            'message': 'The provided date is invalid or malformed'
        }), 400
    
    if not validate_date_format(date_param):
        return jsonify({
            'error': 'INVALID_DATE',
            'message': 'The provided date is invalid or malformed'
        }), 400
    
    try:
        query = text("""
            SELECT id, entry_date, achievement_text, created_at
            FROM f_00baa1bc__daily_wins
            WHERE entry_date = :entry_date
            LIMIT 1
        """)
        
        result = db.session.execute(query, {'entry_date': date_param}).fetchone()
        
        if result:
            entry = {
                'id': result[0],
                'entry_date': result[1].strftime('%Y-%m-%d') if hasattr(result[1], 'strftime') else str(result[1]),
                'achievement_text': result[2],
                'created_at': result[3].isoformat() if hasattr(result[3], 'isoformat') else str(result[3])
            }
            return jsonify({
                'exists': True,
                'entry': entry
            }), 200
        else:
            return jsonify({
                'exists': False,
                'entry': None
            }), 200
            
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({
            'error': 'DATABASE_ERROR',
            'message': 'Failed to query win entries'
        }), 500


@blueprint.post('/api/capability_duplicate_entry_prevention_00baa1bc/wins')
def create_win_with_duplicate_check():
    """
    Attempts to create a new win entry after verifying no duplicate exists 
    for the given date, enforcing the one-per-day constraint.
    
    Request Body:
        achievement_text: The student's achievement text (1-150 characters)
        entry_date: The date for which this win is being recorded (YYYY-MM-DD)
        
    Returns:
        JSON response with success flag and win data, or error
    """
    try:
        data = request.get_json()
    except Exception:
        return jsonify({
            'error': 'INVALID_INPUT',
            'message': 'Achievement text must be between 1 and 150 characters'
        }), 400
    
    if not data:
        return jsonify({
            'error': 'INVALID_INPUT',
            'message': 'Achievement text must be between 1 and 150 characters'
        }), 400
    
    achievement_text = data.get('achievement_text')
    entry_date = data.get('entry_date')
    
    # Validate achievement text
    if not validate_achievement_text(achievement_text):
        return jsonify({
            'error': 'INVALID_INPUT',
            'message': 'Achievement text must be between 1 and 150 characters'
        }), 400
    
    # Validate date format
    if not entry_date or not validate_date_format(entry_date):
        return jsonify({
            'error': 'INVALID_DATE',
            'message': 'The provided date is invalid or malformed'
        }), 400
    
    try:
        # Check for duplicate entry
        check_query = text("""
            SELECT id
            FROM f_00baa1bc__daily_wins
            WHERE entry_date = :entry_date
            LIMIT 1
        """)
        
        existing = db.session.execute(check_query, {'entry_date': entry_date}).fetchone()
        
        if existing:
            return jsonify({
                'error': 'DUPLICATE_ENTRY',
                'message': "Today's win is already recorded. Come back tomorrow."
            }), 409
        
        # Create new win entry
        win_id = str(uuid.uuid4())
        created_at = datetime.utcnow()
        
        insert_query = text("""
            INSERT INTO f_00baa1bc__daily_wins (id, entry_date, achievement_text, created_at)
            VALUES (:id, :entry_date, :achievement_text, :created_at)
        """)
        
        db.session.execute(insert_query, {
            'id': win_id,
            'entry_date': entry_date,
            'achievement_text': achievement_text,
            'created_at': created_at
        })
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'win': {
                'id': win_id,
                'entry_date': entry_date,
                'achievement_text': achievement_text,
                'created_at': created_at.isoformat()
            }
        }), 201
        
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({
            'error': 'DATABASE_ERROR',
            'message': 'Failed to create win entry'
        }), 500
