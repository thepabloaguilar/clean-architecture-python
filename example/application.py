from flask import Flask

from .entrypoints.rest.health import health_bp
from .entrypoints.rest.broadband_access_device import broadband_access_device_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(health_bp)
    app.register_blueprint(broadband_access_device_bp)

    return app
