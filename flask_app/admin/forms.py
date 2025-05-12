"""
TODOC
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, SubmitField,\
    TextAreaField, DateField, ValidationError
from wtforms.validators import DataRequired
import sqlalchemy as sa
from flask_app import db
from flask_app.data_models import Institution, Account, Tag


class TagForm(FlaskForm):
    """
    TODOC
    """
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Save')

    def validate_name(self, name):
        """
        TODOC
        """
        user = db.session.scalar(sa.select(Tag).where(
            Tag.name == name.data))
        if user is not None:
            raise ValidationError('This Tag already exists.')


class InstitutionForm(FlaskForm):
    """
    TODOC
    """
    name = StringField('Name', validators=[DataRequired()])
    tags = SelectMultipleField('Tags')
    submit = SubmitField('Save')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tags.choices = self.get_tags()

    def get_tags(self):
        tag_list = []
        tags = db.session.scalars(sa.select(Tag)).all()
        for t in tags:
            tag_list.append((t.id, t.name))
        return tag_list

    def validate_name(self, name):
        """
        TODOC
        """
        user = db.session.scalar(sa.select(Institution).where(
            Institution.name == name.data))
        if user is not None:
            raise ValidationError('Institution with this name already exists.')

class AccountForm(FlaskForm):
    """
    TODOC
    """
    name = StringField('Name', validators=[DataRequired()])
    acct_type = SelectField('Type', validators=[DataRequired()])
    tags = SelectMultipleField('Tags', validators=[DataRequired()])
    institution = SelectField('Institution', validators=[DataRequired()])
    acct_number = StringField('Account Number')
    comment = TextAreaField('Comment')
    abbreviation = StringField('Abbreviation')
    date_open = DateField('Date Open')
    date_closed = DateField('Date Closed')
    submit = SubmitField('Save')

    def validate_name(self, name):
        """
        TODOC
        """
        user = db.session.scalar(sa.select(Account).where(
            Account.name == name.data))
        if user is not None:
            raise ValidationError('Account with this name already exists.')


# class PayeeForm(FlaskForm):
#     """
#     TODOC
#     """
#     name = StringField('Name', validators=[DataRequired()])
#     submit = SubmitField('Save')

#     def validate_name(self, name):
#         """
#         TODOC
#         """
#         user = db.session.scalar(sa.select(Payee).where(
#             Payee.name == name.data))
#         if user is not None:
#             raise ValidationError('Payee with this name already exists.')
