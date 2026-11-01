from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    from fabric_store import db
    db.init_app(app)
    from . import health
    app.register_blueprint(health.bp)
    return app