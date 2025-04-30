"""
TODOC
Contains the main flow control for this entire operation here.


Created by:   Joshua Meade
Created on:   3/16/2025
"""

import sqlalchemy
import sqlalchemy.orm
from flask_app import create_app

app = create_app()

@app.shell_context_processor
def shell_context():
    """
    Sets context and available libraries for the Flask shell sub-command.
    """
    return {
        "sa": sqlalchemy,
        "so": sqlalchemy.orm
    }
