"""Safe API error mapping with useful recovery messages."""
from flask import current_app, jsonify
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from werkzeug.exceptions import HTTPException

from backend.core.wins import InputError


def register_error_handlers(app):
    @app.errorhandler(InputError)
    def invalid_input(error):
        return jsonify(error="INVALID_INPUT", message=str(error)), 400

    @app.errorhandler(IntegrityError)
    def integrity_error(error):
        current_app.logger.exception("Database constraint failed")
        return jsonify(error="CONFLICT", message="This record already exists."), 409

    @app.errorhandler(SQLAlchemyError)
    def database_error(error):
        current_app.logger.exception("Database operation failed")
        return jsonify(error="DATABASE_ERROR", message="Unable to save or load records. Please try again."), 503

    @app.errorhandler(HTTPException)
    def http_error(error):
        return jsonify(error=error.name, message=error.description), error.code
