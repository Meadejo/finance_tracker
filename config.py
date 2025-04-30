"""
TODOC
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    TODOC
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fuck-me-in-the-ass-with-a-posthole-digger'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database/test.db')
