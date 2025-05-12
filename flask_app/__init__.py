"""
TODOC
"""
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from config import Config


# Instanciate our bullshit
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
mail = Mail()
moment = Moment()

# Set up how we launch our app
def create_app(config_class=Config):
    """
    TODOC
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    moment.init_app(app)

    # Import Blueprints
    # We're importing down here to prevent circular dependencies.
    from flask_app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from flask_app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from flask_app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    from flask_app.admin import bp as admin_bp
    app.register_blueprint(admin_bp)
    from flask_app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    # If we're not running in Debug mode, enable logging.
    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240,
                                        backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Application startup')

    return app

# And finally, we're importing models down here for more circular dependency prevention.
from flask_app import data_models
