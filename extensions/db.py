import config
import os
from flask_sqlalchemy import SQLAlchemy

# UPPER CASE vars: Vars from config.py
# app.config vars:


class DB:
    db = None
    engines = {}
    cfg = config.config

    def __init__(self):
        pass

    @staticmethod
    def init_app(app):
        env = None
        try:
            env = os.environ['FLASK_ENV']  # getattr(config, 'ENV', False)
        except Exception as e:
            print(str(e))

        app.config['SQLALCHEMY_DATABASE_URI'] = config.config.get(
            "DATABASE_CONNECTION_STRING")
        if env == 'development':
            app.config['SQLALCHEMY_DATABASE_URI'] = config.config.get(
                "DBCONN_STRING_DEV")

        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_BINDS'] = {
            'default': config.config.get("DATABASE_CONNECTION_STRING"),
            'dev': config.config.get("DBCONN_STRING_DEV"),
            'prod': config.config.get("DATABASE_CONNECTION_STRING")
        }

        DB.db = SQLAlchemy(app)
        DB.engines['default'] = DB.db.engine
        DB.engines['prod'] = DB.db.get_engine(app, "prod")
        DB.engines['dev'] = DB.db.get_engine(app, "dev")
