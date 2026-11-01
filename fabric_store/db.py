import psycopg
from flask import current_app, g

def _connect():
    cfg = current_app.config
    return psycopg.connect(
        host=cfg["DB_HOST"], port=cfg["DB_PORT"], dbname=cfg["DB_NAME"],
        user=cfg["DB_USER"], password=cfg["DB_PASSWORD"]
    )

def get_db():
    if "db" not in g:
        g.db = _connect()
    return g.db

def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
