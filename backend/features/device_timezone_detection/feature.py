"""Device timezone detection feature module."""
import uuid
from datetime import datetime, date
from flask import Blueprint, request, jsonify
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from db import get_db

blueprint = Blueprint('capability_device_timezone_detection_aca07cc7', __name__)


def validate_date_format(date_string):
    """Validate that a string is in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except (ValueError, TypeError):
        return False


def validate_uuid_format(uuid_string):
    """Validate that a string is a valid UUID."""
    try:
        uuid.UUID(uuid_string)
        return True
    except (ValueError, TypeError, AttributeError):
        return False


@blueprint.get('/api/capability_device_timezone_detection_aca07cc7/local-date/current')
def get_current_local_date():
    """
    Reads the device's local calendar date from the client and returns it to enable timezone-aware operations.
    
    Returns:
        JSON response with local_date in YYYY-MM-DD format
    """
    try:
        # Get the current UTC date as a fallback/default
        # In a real implementation, this would typically receive the client's local date
        # from a request parameter or header, but per the spec, this endpoint takes no parameters
        # and returns the current date. We'll use server time as the implementation.
        local_date = date.today().isoformat()
        
        if not validate_date_format(local_date):
            return jsonify({
                'error': 'INVALID_DATE',
                'message': 'Unable to determine valid local date from device'
            }), 400
        
        return jsonify({
            'local_date': local_date
        }), 200
    except Exception:
        return jsonify({
            'error': 'INVALID_DATE',
            'message': 'Unable to determine valid local date from device'
        }), 400


@blueprint.post('/api/capability_device_timezone_detection_aca07cc7/local-date/check')
def check_entry_exists_for_date():
    """
    Checks if an achievement entry already exists for a given local date to enforce one-per-day logic and detect midnight rollover.
    
    Request JSON:
        local_date: The local calendar date (YYYY-MM-DD) to check for existing entries
    
    Returns:
        JSON response with exists boolean and optional entry_id
    """
    data = request.get_json()
    
    if not data or 'local_date' not in data:
        return jsonify({
            'error': 'INVALID_DATE_FORMAT',
            'message': 'local_date must be in YYYY-MM-DD format'
        }), 400
    
    local_date = data['local_date']
    
    if not validate_date_format(local_date):
        return jsonify({
            'error': 'INVALID_DATE_FORMAT',
            'message': 'local_date must be in YYYY-MM-DD format'
        }), 400
    
    db = get_db()
    
    query = text("""
        SELECT id, entry_id 
        FROM f_aca07cc7__entry_local_dates 
        WHERE local_date = :local_date 
        LIMIT 1
    """)
    
    result = db.execute(query, {'local_date': local_date}).fetchone()
    
    if result:
        return jsonify({
            'exists': True,
            'entry_id': result[1]
        }), 200
    else:
        return jsonify({
            'exists': False,
            'entry_id': None
        }), 200


@blueprint.post('/api/capability_device_timezone_detection_aca07cc7/local-date/record')
def record_entry_local_date():
    """
    Stores the device's local calendar date for a new achievement entry to associate it with the correct local day.
    
    Request JSON:
        entry_id: The ID of the achievement entry being created
        local_date: The device's local calendar date (YYYY-MM-DD) when the entry was created
    
    Returns:
        JSON response with created record details
    """
    data = request.get_json()
    
    if not data or 'local_date' not in data:
        return jsonify({
            'error': 'INVALID_DATE_FORMAT',
            'message': 'local_date must be in YYYY-MM-DD format'
        }), 400
    
    if 'entry_id' not in data:
        return jsonify({
            'error': 'INVALID_ENTRY_ID',
            'message': 'entry_id must be a valid UUID'
        }), 400
    
    local_date = data['local_date']
    entry_id = data['entry_id']
    
    if not validate_date_format(local_date):
        return jsonify({
            'error': 'INVALID_DATE_FORMAT',
            'message': 'local_date must be in YYYY-MM-DD format'
        }), 400
    
    if not validate_uuid_format(entry_id):
        return jsonify({
            'error': 'INVALID_ENTRY_ID',
            'message': 'entry_id must be a valid UUID'
        }), 400
    
    db = get_db()
    
    # Check if an entry already exists for this local date
    check_query = text("""
        SELECT id 
        FROM f_aca07cc7__entry_local_dates 
        WHERE local_date = :local_date 
        LIMIT 1
    """)
    
    existing = db.execute(check_query, {'local_date': local_date}).fetchone()
    
    if existing:
        return jsonify({
            'error': 'DUPLICATE_LOCAL_DATE',
            'message': 'An entry already exists for this local date'
        }), 409
    
    # Create new record
    record_id = str(uuid.uuid4())
    created_at_utc = datetime.utcnow()
    
    insert_query = text("""
        INSERT INTO f_aca07cc7__entry_local_dates 
        (id, entry_id, local_date, created_at_utc)
        VALUES (:id, :entry_id, :local_date, :created_at_utc)
    """)
    
    try:
        db.execute(insert_query, {
            'id': record_id,
            'entry_id': entry_id,
            'local_date': local_date,
            'created_at_utc': created_at_utc
        })
        db.commit()
    except IntegrityError:
        db.rollback()
        return jsonify({
            'error': 'DUPLICATE_LOCAL_DATE',
            'message': 'An entry already exists for this local date'
        }), 409
    except Exception as e:
        db.rollback()
        return jsonify({
            'error': 'DATABASE_ERROR',
            'message': 'Failed to record entry local date'
        }), 500
    
    return jsonify({
        'id': record_id,
        'entry_id': entry_id,
        'local_date': local_date,
        'created_at_utc': created_at_utc.isoformat() + 'Z'
    }), 200
