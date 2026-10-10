from flask import Blueprint, jsonify, request
from functools import wraps
import logging

logger = logging.getLogger(__name__)

blueprint = Blueprint('single_screen_interface', __name__)


def handle_errors(f):
    """Decorator to handle errors consistently across endpoints."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError as e:
            logger.warning(f"Validation error in {f.__name__}: {str(e)}")
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            logger.error(f"Unexpected error in {f.__name__}: {str(e)}")
            return jsonify({"error": "An unexpected error occurred"}), 500
    return decorated_function


@blueprint.get('/health')
@handle_errors
def health_check():
    """Health check endpoint for single screen interface feature."""
    return jsonify({
        "status": "healthy",
        "feature": "single_screen_interface"
    }), 200
