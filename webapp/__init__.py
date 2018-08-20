from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('webapp.settings')
    app.config.from_object('webapp.secure')
    register_app(app)
    return app


def register_app(app):
    from webapp.web import web

    app.register_blueprint(web, url_prefix='/web')

