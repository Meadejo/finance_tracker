"""
TODOC
"""

import sqlalchemy as sa
from flask import request
# from flask import abort
from flask_app import db
from flask_app.api import bp
from flask_app.api.auth import token_auth
from flask_app.data_models import Account

@bp.route('/account/<int:id>', methods=['GET'])
@token_auth.login_required
def get_account(id):
    """
    TODOC
    """
    return db.get_or_404(Account, id).to_dict()

@bp.route('/account', methods=['GET'])
@token_auth.login_required
def get_accounts():
    """
    TODOC
    """
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    return Account.to_collection_dict(sa.select(Account), page, per_page, 'api.get_accounts')

@bp.route('/account', methods=['POST'])
@token_auth.login_required
def create_account():
    """
    TODOC
    """
    # TODO
    pass

@bp.route('/account/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_account(id):
    """
    TODOC
    """
    # TODO
    pass

# @bp.route('/users/<int:id>', methods=['PUT'])
# @token_auth.login_required
# def update_user(id):
#     if token_auth.current_user().id != id:
#         abort(403)
