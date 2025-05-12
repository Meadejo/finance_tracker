"""
TODOC
"""

from flask_app import db
from flask_app.api import bp
from flask_app.api.auth import basic_auth, token_auth

@bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    """
    TODOC
    """
    token = basic_auth.current_user().get_token()
    db.session.commit()
    return token

@bp.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    """
    TODOC
    """
    token_auth.current_user().revoke_token()
    db.session.commit()
    return '', 204
