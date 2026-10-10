"""
Flask Blueprint module for recording daily achievements.

This module provides endpoints to check if an achievement exists for today
and to save a new daily achievement with validation.
"""

from flask import Blueprint, request, jsonify
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from datetime import date, datetime
import uuid

# Assuming db is imported from the application factory or a shared module
# from app import db
# For this module, we'll import it as needed
from extensions import db

blueprint = Blueprint('capability_record_daily_achievement_86a57805', __name__)


@blueprint.get('/api/capability_record_daily_achievement_86a57805/achievements/today')
def check_today_entry():
    """
    Checks if an achievement entry already exists for the current date
    to enforce the one-entry-per-day constraint.
    
    Returns:
        JSON response with exists flag and optional achievement data
    """
    try:
        today = date.today()
        
        query = text("""
            SELECT id, achievement_text, recorded_date, created_at
            FROM f_86a57805__achievements
            WHERE recorded_date = :today
            LIMIT 1
        """)
        
        result = db.session.execute(query, {'today': today}).fetchone()
        
        if result:
            achievement = {
                'id': result[0],
                'achievement_text': result[1],
                'recorded_date': result[2].isoformat(),
                'created_at': result[3].isoformat()
            }
            return jsonify({
                'exists': True,
                'achievement': achievement
            }), 200
        else:
            return jsonify({
                'exists': False,
                'achievement': None
            }), 200
            
    except SQLAlchemyError as e:
        return jsonify({
            'code': 'STORAGE_ERROR',
            'message': 'Failed to check today\'s entry'
        }), 500


@blueprint.post('/api/capability_record_daily_achievement_86a57805/achievements')
def save_achievement():
    """
    Saves a new daily achievement entry to storage with validation
    for text length and one-entry-per-day constraint enforcement.
    
    Returns:
        JSON response with the saved achievement data
    """
    try:
        data = request.get_json()
        
        if not data or 'achievement_text' not in data:
            return jsonify({
                'code': 'VALIDATION_ERROR',
                'message': 'Achievement text must be between 1 and 150 characters'
            }), 400
        
        achievement_text = data.get('achievement_text', '')
        
        # Validate text length
        if not achievement_text or len(achievement_text) < 1 or len(achievement_text) > 150:
            return jsonify({
                'code': 'VALIDATION_ERROR',
                'message': 'Achievement text must be between 1 and 150 characters'
            }), 400
        
        today = date.today()
        
        # Check if an entry already exists for today
        check_query = text("""
            SELECT id
            FROM f_86a57805__achievements
            WHERE recorded_date = :today
            LIMIT 1
        """)
        
        existing = db.session.execute(check_query, {'today': today}).fetchone()
        
        if existing:
            return jsonify({
                'code': 'DUPLICATE_ENTRY',
                'message': 'An achievement has already been recorded for today'
            }), 409
        
        # Generate UUID and timestamp
        achievement_id = str(uuid.uuid4())
        created_at = datetime.utcnow()
        
        # Insert the new achievement
        insert_query = text("""
            INSERT INTO f_86a57805__achievements (id, achievement_text, recorded_date, created_at)
            VALUES (:id, :achievement_text, :recorded_date, :created_at)
        """)
        
        db.session.execute(insert_query, {
            'id': achievement_id,
            'achievement_text': achievement_text,
            'recorded_date': today,
            'created_at': created_at
        })
        db.session.commit()
        
        # Return the saved achievement
        return jsonify({
            'id': achievement_id,
            'achievement_text': achievement_text,
            'recorded_date': today.isoformat(),
            'created_at': created_at.isoformat()
        }), 201
        
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({
            'code': 'STORAGE_ERROR',
            'message': 'Failed to save achievement'
        }), 500
