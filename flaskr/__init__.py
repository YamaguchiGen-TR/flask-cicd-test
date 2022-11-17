from flask import Flask
from flaskr.routes import api


def create_app() -> Flask:
    # Flask
    app = Flask(__name__)

    # Flask RestX
    # https://flask-restx.readthedocs.io/en/latest/configuration.html
    app.config['RESTX_VALIDATE'] = True
    app.config['RESTX_MASK_SWAGGER'] = False
    app.config['RESTX_ERROR_404_HELP'] = False
    api.init_app(app)

    return app
