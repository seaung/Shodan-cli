from flask import Flask

def create_app():
    app = Flask(__name__)
    register_app(app)
    return app


def register_app(app):
    from webapp.web import web

    app.register_blueprint(web, url_prefix='/web')

