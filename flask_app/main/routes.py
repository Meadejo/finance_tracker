"""
TODOC
"""

from datetime import datetime, timezone
from flask import render_template
from flask_login import current_user, login_required
from flask_app import db
from flask_app.main import bp

@bp.before_app_request
def before_request():
    """
    TODOC
    """
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(timezone.utc)
        db.session.commit()

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    """
    TODOC
    """
    return render_template('index.html', title='Home')

@bp.route('/lol')
@login_required
def lol():
    """
    TODOC
    """
    return render_template('lol.html')
