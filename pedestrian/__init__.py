import os

from flask import Flask
from pedestrian.settings import config
from pedestrian.blueprints.auth import auth_bp
from pedestrian.blueprints.console import console_bp
from pedestrian.blueprints.site import site_bp


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('pedestrian')
    app.config.from_object(config[config_name])

    register_blueprints(app)
    register_commands(app)
    register_extensions(app)

    return app


def regsiter_logging(app):
    pass


def register_extensions(app):
    pass


def register_blueprints(app):
    app.register_blueprint(site_bp)
    app.register_blueprint(auth_bp, subdomain='auth')
    app.register_blueprint(console_bp, subdomain='console')
    pass


def register_commands(app):
    pass
