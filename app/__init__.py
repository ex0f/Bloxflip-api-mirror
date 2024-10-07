from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import mirror_endpoint
    app.register_blueprint(mirror_endpoint)

    return app
