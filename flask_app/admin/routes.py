"""
TODOC
"""

# from datetime import datetime, timezone
from flask import render_template
from flask_login import login_required
# import sqlalchemy as sa
import flask_app.ui_models as ui
from flask_app import db
from flask_app.data_models import Institution, Account, Tag
from flask_app.ui_models import Table
from flask_app.main import data_shaping
from flask_app.admin import bp
from flask_app.admin.forms import InstitutionForm, AccountForm, TagForm


@bp.route('/admin')
@login_required
def index():
    """
    TODOC
    """
    list_items = ui.admin_index_list()
    return render_template('admin/index.html', title='Admin', list_items=list_items)


@bp.route('/admin/tags', methods=['GET', 'POST'])
@login_required
def tags():
    """
    TODOC
    """
    form = TagForm()
    table = Table(
        id="taglist",
        data = Tag.query.all(),
        type="list_edit"
    )
    if form.validate_on_submit():
        t = Tag(name=form.name.data)
        db.session.add(t)
        db.session.commit()
        table = Table(
            id="taglist",
            data = Tag.query.all(),
            type="list_edit"
        )
        return render_template('admin/list_edit.html', title='Tags',
                           form=form, table=table)
    return render_template('admin/list_edit.html', title='Tags',
                           form=form, table=table)


@bp.route('/admin/institutions', methods=['GET', 'POST'])
@login_required
def institutions():
    """
    TODOC
    """
    form = InstitutionForm()
    institution_list = Institution.query.all()
    table_data = data_shaping.admin_list_edit(institution_list)
    if form.validate_on_submit():
        i = Institution(
            name=form.name.data
        )
        db.session.add(i)
        db.session.commit()
        institution_list = Institution.query.all()
        table_data = data_shaping.admin_list_edit(institution_list)
        return render_template('admin/list_edit.html', title='Institutions',
                           form=form, table_data=table_data)
    return render_template('admin/list_edit.html', title='Institutions',
                           form=form, table_data=table_data)


@bp.route('/admin/accounts', methods=['GET', 'POST'])
@login_required
def accounts():
    """
    TODOC
    """
    form = AccountForm()
    table = Table(
        id="accountlist",
        entity=Account
    )
    # account_list = Account.query.all()
    # table_data = data_shaping.admin_list_edit(account_list)
    if form.validate_on_submit():
        a = Account(
            name=form.name.data
            # TODO Complete this form
        )
        db.session.add(a)
        db.session.commit()
        # account_list = Account.query.all()
        # table_data = data_shaping.admin_list_edit(account_list)
        table = Table(
            id="accountlist",
            data = Account.query.all(),
            type="list_edit"
        )
        return render_template('admin/list_edit.html', title='Accounts',
                           form=form, table=table)
    return render_template('admin/list_edit.html', title='Accounts',
                           form=form, table=table)
