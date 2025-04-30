"""
TODOC
"""

from datetime import datetime, timezone
from flask import render_template
from flask_login import current_user, login_required
from flask_app import db
from flask_app.admin import bp

@bp.route('/admin')
@login_required
def index():
    """
    TODOC
    """
    return render_template('admin/index.html', title='Admin')
