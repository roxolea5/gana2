import datetime
from flask import Flask
from flask_cors import CORS
from flask_session import Session
from flask_jwt import JWT
from flask_jwt_extended import JWTManager

import os

from config import config


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

        self.app.config['CORS_HEADERS'] = 'Content-Type'
        CORS(self.app, resources={r"/api/*": {"origins": "*"}})

        self.register_extensions()
        self.register_blueprints()

        self.register_jwt()

    def register_extensions(self):
        from extensions.db import DB
        DB.init_app(self.app)

    def register_blueprints(self):
        from blueprints.web import web_api
        self.app.register_blueprint(web_api)
        from blueprints.usuarios import usuarios_api
        self.app.register_blueprint(usuarios_api)
        from blueprints.razas import razas_api
        self.app.register_blueprint(razas_api)
        from blueprints.propietarios import propietarios_api
        self.app.register_blueprint(propietarios_api)
        from blueprints.roles import roles_api
        self.app.register_blueprint(roles_api)
        from blueprints.colores import colores_api
        self.app.register_blueprint(colores_api)
        from blueprints.destinos import destinos_api
        self.app.register_blueprint(destinos_api)
        from blueprints.diagnosticos_palpado import diagnosticos_palpado_api
        self.app.register_blueprint(diagnosticos_palpado_api)
        from blueprints.tipo_movimientos import tipo_movimientos_api
        self.app.register_blueprint(tipo_movimientos_api)
        from blueprints.paises import paises_api
        self.app.register_blueprint(paises_api)
        from blueprints.estados import estados_api
        self.app.register_blueprint(estados_api)
        from blueprints.municipios import municipios_api
        self.app.register_blueprint(municipios_api)
        from blueprints.localidades import localidades_api
        self.app.register_blueprint(localidades_api)
        from blueprints.ranchos import ranchos_api
        self.app.register_blueprint(ranchos_api)
        from blueprints.potreros import potreros_api
        self.app.register_blueprint(potreros_api)
        from blueprints.lotes import lotes_api
        self.app.register_blueprint(lotes_api)
        from blueprints.auth import auth_api
        self.app.register_blueprint(auth_api)
        from blueprints.personas import personas_api
        self.app.register_blueprint(personas_api)
        from blueprints.rolesusuario import roles_usuario_api
        self.app.register_blueprint(roles_usuario_api)
        from blueprints.usuario_persona import usuario_persona_api
        self.app.register_blueprint(usuario_persona_api)

    def register_jwt(self):
        self.app.config['SECRET_KEY'] = config['JWT_SECRET_KEY']
        self.jwt = JWTManager(self.app)


if __name__ == '__main__':
    app = Gana2().app

    # export FLASK_ENV=development
    if 'ssl_context' in config:
        app.run(threaded=True, debug=True,
                port=config['port'], host=config['host'], ssl_context=config['ssl_context'])
    else:
        app.run(threaded=True, debug=True,
                port=config['port'], host=config['host'])
