"""
TODOC
"""

from flask import render_template
from flask_app import db
from flask_app.errors import bp

@bp.app_errorhandler(404)
def not_found_error(error):
    """
    TODOC
    """
    # TODO Log error details
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    """
    TODOC
    """
    # TODO Log error details
    db.session.rollback()
    return render_template('errors/500.html'), 500
