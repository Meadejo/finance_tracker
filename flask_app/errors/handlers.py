"""
TODOC
"""

from flask import render_template, request
from flask_app import db
from flask_app.errors import bp
from flask_app.api.errors import error_response as api_error_response

def wants_json_response():
    """
    TODOC
    """
    return request.accept_mimetypes['application/json'] >= \
        request.accept_mimetypes['text/html']

@bp.app_errorhandler(404)
def not_found_error(error):
    """
    TODOC
    """
    if wants_json_response():
        return api_error_response(404)
    # TODO Log error details
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    """
    TODOC
    """
    # TODO Log error details
    db.session.rollback()
    if wants_json_response():
        return api_error_response(500)
    return render_template('errors/500.html'), 500
