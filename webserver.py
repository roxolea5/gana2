import datetime

from config import config
from flask import Flask
from flask_session import Session


class Gana2:

    app = None

    def __init__(self):
        self.app = Flask(__name__, static_url_path="")
        self.app.url_map.strict_slashes = False
        self.app.config['SECRET_KEY'] = config['secret_key']
        self.app.config['REMEMBER_COOKIE_SECURE'] = True
        self.app.config['SESSION_COOKIE_SECURE'] = True
        Session(self.app)
        Session.permanent = True
        self.app.permanent_session_lifetime = datetime.timedelta(days=180)

        self.register_extensions()
        self.register_blueprints()

    def register_extensions(self):
        from extensions.db import DB
        DB.init_app(self.app)

    def register_blueprints(self):
        from blueprints.web import web_api
        self.app.register_blueprint(web_api)
        from blueprints.razas import razas_api
        self.app.register_blueprint(razas_api)
        from blueprints.propietarios import propietarios_api
        self.app.register_blueprint(propietarios_api)
        from blueprints.roles import roles_api
        self.app.register_blueprint(roles_api)


if __name__ == '__main__':
    app = Gana2().app
    if 'ssl_context' in config:
        app.run(threaded=True, debug=True,
                port=config['port'], host=config['host'], ssl_context=config['ssl_context'])
    else:
        app.run(threaded=True, debug=True,
                port=config['port'], host=config['host'])
