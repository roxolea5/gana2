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
        env = getattr(config, 'ENV', False)

        app.config['SQLALCHEMY_DATABASE_URI'] = config.config.get(
            "DATABASE_CONNECTION_STRING")
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_BINDS'] = {
            'default': config.config.get("DATABASE_CONNECTION_STRING"),
            'dev': config.config.get("DBCONN_STRING_DEV"),
            'prod': config.config.get("DATABASE_CONNECTION_STRING")
        }

        # if env is local

        if env == 'local':
            app.config['SQLALCHEMY_BINDS']['dev'] = config.DATABASE_CONNECTION_STRING

        DB.db = SQLAlchemy(app)
        DB.engines['default'] = DB.db.engine
        DB.engines['prod'] = DB.db.get_engine(app, "prod")
        DB.engines['dev'] = DB.db.get_engine(app, "dev")

        # if env is local
        if env == 'local':
            DB.engines['dev'] = DB.db.get_engine(app, "dev")
