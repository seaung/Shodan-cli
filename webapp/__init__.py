from flask import Flask
from webapp.web import web

def create_app():
    app = Flask(__name__)
    register_app(app)
    return app


def register_app(app):

    app.register_blueprint(web, url_prefix='/web')

