"""
TODOC
"""

from flask import render_template, current_app
from flask_app.email import send_email


def send_password_reset_email(user):
    """
    TODOC
    """
    token = user.get_reset_password_token()
    send_email('Reset Your Cash Money Password',
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))
