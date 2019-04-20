from flask import Flask


def register_blueprints(app):
    from ShodanApp.blueprints import mshodan
    app.register_blueprint(mshodan)


def create_app():
    app = Flask(__name__)
    app.config.from_object('ShodanApp.config.settings')
    app.config.from_object('ShodanApp.config.security')
    register_blueprints(app)
    return app
