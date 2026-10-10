"""
One entry per day limit feature module.
Enforces the constraint that only one win entry is allowed per calendar day.
"""

from flask import Blueprint, request, jsonify
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import uuid
import os
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

# Create Blueprint
blueprint = Blueprint('capability_one_entry_per_day_limit_86f08838', __name__)

# Database connection
def get_db_engine():
    """Get database engine from environment variables."""
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_user = os.environ.get('DB_USER', 'root')
    db_password = os.environ.get('DB_PASSWORD', '')
    db_name = os.environ.get('DB_NAME', 'app_db')
    db_port = os.environ.get('DB_PORT', '3306')
    
    connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    return create_engine(connection_string, poolclass=NullPool)

def validate_date_format(date_string):
    """Validate that date_string is in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except (ValueError, TypeError):
        return False

def validate_timestamp_format(timestamp_string):
    """Validate that timestamp_string is a valid ISO 8601 timestamp."""
    try:
        datetime.fromisoformat(timestamp_string.replace('Z', '+00:00'))
        return True
    except (ValueError, TypeError, AttributeError):
        return False


@blueprint.route('/api/capability_one_entry_per_day_limit_86f08838/daily-wins/check', methods=['GET'])
def check_entry_exists_for_date():
    """
    Checks if a win entry already exists for a given calendar date.
    Returns existence status to enforce the one-entry-per-day constraint.
    """
    entry_date = request.args.get('entry_date')
    
    # Validate date format
    if not entry_date or not validate_date_format(entry_date):
        return jsonify({
            'error': 'INVALID_DATE_FORMAT',
            'message': 'The entry_date must be in YYYY-MM-DD format'
        }), 400
    
    engine = get_db_engine()
    
    try:
        with engine.connect() as connection:
            query = text("""
                SELECT COUNT(*) as count
                FROM f_86f08838__daily_win_entries
                WHERE entry_date = :entry_date
            """)
            result = connection.execute(query, {'entry_date': entry_date})
            row = result.fetchone()
            exists = row[0] > 0
            
            return jsonify({
                'exists': exists,
                'entry_date': entry_date
            }), 200
    except Exception as e:
        return jsonify({
            'error': 'DATABASE_ERROR',
            'message': str(e)
        }), 500


@blueprint.route('/api/capability_one_entry_per_day_limit_86f08838/daily-wins', methods=['POST'])
def create_daily_win_entry():
    """
    Creates a new win entry for a specific calendar date.
    Enforces the one-entry-per-day constraint by rejecting creation if an entry already exists.
    """
    data = request.get_json()
    
    if not data:
        return jsonify({
            'error': 'INVALID_REQUEST',
            'message': 'Request body must be valid JSON'
        }), 400
    
    achievement_text = data.get('achievement_text')
    entry_date = data.get('entry_date')
    created_at = data.get('created_at')
    
    # Validate achievement_text
    if not achievement_text or not isinstance(achievement_text, str):
        return jsonify({
            'error': 'INVALID_ACHIEVEMENT_TEXT',
            'message': 'Achievement text must be between 1 and 150 characters'
        }), 400
    
    if len(achievement_text) < 1 or len(achievement_text) > 150:
        return jsonify({
            'error': 'INVALID_ACHIEVEMENT_TEXT',
            'message': 'Achievement text must be between 1 and 150 characters'
        }), 400
    
    # Validate date format
    if not entry_date or not validate_date_format(entry_date):
        return jsonify({
            'error': 'INVALID_DATE_FORMAT',
            'message': 'The entry_date must be in YYYY-MM-DD format'
        }), 400
    
    # Validate timestamp format
    if not created_at or not validate_timestamp_format(created_at):
        return jsonify({
            'error': 'INVALID_TIMESTAMP_FORMAT',
            'message': 'The created_at must be a valid ISO 8601 timestamp'
        }), 400
    
    # Generate UUID for the entry
    entry_id = str(uuid.uuid4())
    
    engine = get_db_engine()
    
    try:
        with engine.connect() as connection:
            # Check if entry already exists for this date
            check_query = text("""
                SELECT COUNT(*) as count
                FROM f_86f08838__daily_win_entries
                WHERE entry_date = :entry_date
            """)
            result = connection.execute(check_query, {'entry_date': entry_date})
            row = result.fetchone()
            
            if row[0] > 0:
                return jsonify({
                    'error': 'ENTRY_ALREADY_EXISTS',
                    'message': 'A win entry already exists for this date. Only one entry per calendar day is allowed.'
                }), 409
            
            # Insert new entry
            insert_query = text("""
                INSERT INTO f_86f08838__daily_win_entries
                (id, entry_date, achievement_text, created_at)
                VALUES (:id, :entry_date, :achievement_text, :created_at)
            """)
            
            # Parse the ISO timestamp to MySQL compatible format
            created_at_dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
            
            connection.execute(insert_query, {
                'id': entry_id,
                'entry_date': entry_date,
                'achievement_text': achievement_text,
                'created_at': created_at_dt
            })
            connection.commit()
            
            return jsonify({
                'id': entry_id,
                'achievement_text': achievement_text,
                'entry_date': entry_date,
                'created_at': created_at
            }), 201
            
    except IntegrityError:
        # Handle race condition where entry was created between check and insert
        return jsonify({
            'error': 'ENTRY_ALREADY_EXISTS',
            'message': 'A win entry already exists for this date. Only one entry per calendar day is allowed.'
        }), 409
    except Exception as e:
        return jsonify({
            'error': 'DATABASE_ERROR',
            'message': str(e)
        }), 500


@blueprint.route('/api/capability_one_entry_per_day_limit_86f08838/daily-wins/<entry_date>', methods=['GET'])
def get_entry_for_date(entry_date):
    """
    Retrieves the win entry for a specific calendar date if one exists.
    Used to display existing entries and verify the one-entry-per-day constraint.
    """
    # Validate date format
    if not validate_date_format(entry_date):
        return jsonify({
            'error': 'INVALID_DATE_FORMAT',
            'message': 'The entry_date must be in YYYY-MM-DD format'
        }), 400
    
    engine = get_db_engine()
    
    try:
        with engine.connect() as connection:
            query = text("""
                SELECT id, entry_date, achievement_text, created_at
                FROM f_86f08838__daily_win_entries
                WHERE entry_date = :entry_date
            """)
            result = connection.execute(query, {'entry_date': entry_date})
            row = result.fetchone()
            
            if not row:
                return jsonify({
                    'error': 'ENTRY_NOT_FOUND',
                    'message': 'No win entry exists for the specified date'
                }), 404
            
            # Convert created_at to ISO 8601 format
            created_at_iso = row[3].isoformat() if isinstance(row[3], datetime) else row[3]
            
            return jsonify({
                'id': row[0],
                'entry_date': str(row[1]),
                'achievement_text': row[2],
                'created_at': created_at_iso
            }), 200
            
    except Exception as e:
        return jsonify({
            'error': 'DATABASE_ERROR',
            'message': str(e)
        }), 500
