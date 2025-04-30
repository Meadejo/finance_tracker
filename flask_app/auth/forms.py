"""
TODOC
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa
from flask_app import db
from flask_app.data_models import User


class RegistrationForm(FlaskForm):
    """
    TODOC
    """
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """
        TODOC
        """
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        """
        TODOC
        """
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')


class LoginForm(FlaskForm):
    """
    TODOC
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class ResetPasswordRequestForm(FlaskForm):
    """
    TODOC
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    """
    TODOC
    """
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField('Request Password Reset')
