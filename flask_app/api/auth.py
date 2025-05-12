"""
TODOC
"""

import sqlalchemy as sa
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask_app import db
from flask_app.data_models import User
from flask_app.api.errors import error_response

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username, password):
    """
    TODOC
    """
    user = db.session.scalar(sa.select(User).where(User.username == username))
    if user and user.check_password(password):
        return user

@basic_auth.error_handler
def basic_auth_error(status):
    """
    TODOC
    """
    return error_response(status)

@token_auth.verify_token
def verify_token(token):
    """
    TODOC
    """
    return User.check_token(token) if token else None

@token_auth.error_handler
def token_auth_error(status):
    """
    TODOC
    """
    return error_response(status)
