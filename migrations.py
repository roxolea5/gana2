import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.config.get('DBCONN_STRING_DEV')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


class User(db.Model):
    __tablename__ = 'adm_usuarios'
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)

    username = db.Column(db.String(255), unique=True, default=None)
    password = db.Column(db.String(255), nullable=False, default=None)
    session_id = db.Column(db.String(70), default=None)
    correo_electronico = db.Column(db.String(255), unique=True, default=None)
    usuario_creacion_id = db.Column(db.Integer, default=None)
    fecha_creacion = db.Column(
        db.DateTime(), default=None)
    usuario_modificacion_id = db.Column(db.Integer, default=None)
    fecha_modificacion = db.Column(
        db.DateTime(), default=None)
    active = db.Column(db.Boolean(), default=None)
    propietario_id = db.Column(db.Integer, db.ForeignKey(
        'adm_propietarios.id'), default=None)

    adm_rol_usuario = db.relationship('AdmRolUsuario')
    adm_usuario_persona = db.relationship('AdmUsuarioPersona')


class AdmPersona(db.Model):
    __tablename__ = 'adm_personas'
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)

    tipo_persona = db.Column(db.Boolean(4), default=None)
    curp = db.Column(db.String(18), default=None)
    rfc = db.Column(db.String(25), default=None)
    nombre = db.Column(db.String(75), default=None)
    apellido_paterno = db.Column(db.String(150), default=None)
    apellido_materno = db.Column(db.String(150), default=None)
    direccion = db.Column(db.Text)
    estado_id = db.Column(db.Integer, db.ForeignKey(
        'cat_estados.id'), default=None)
    municipio_id = db.Column(db.Integer, default=None)
    localidad_id = db.Column(db.Integer, default=None)
    activo = db.Column(db.Boolean(4), default=1)
    usuario_creacion_id = db.Column(db.Integer, nullable=False, default=1)
    fecha_creacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    usuario_modificacion_id = db.Column(db.Integer, nullable=False, default=1)
    fecha_modificacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    propietario_id = db.Column(db.Integer, default=None)

    adm_usuario_persona = db.relationship('AdmUsuarioPersona')


class AdmPropietario(db.Model):
    __tablename__ = 'adm_propietarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    correo_electronico = db.Column(
        db.String(100), nullable=False)
    activo = db.Column(db.Boolean(4))
    identificador = db.Column(db.String(250), default=None)

    rancho = db.relationship('Rancho')
    usuario = db.relationship('User')


class AdmRol(db.Model):
    __tablename__ = 'adm_roles'

    rol = db.Column(db.String(50), primary_key=True, nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    activo = db.Column(db.Boolean(4))

    adm_rol_usuario = db.relationship('AdmRolUsuario')


class AdmRolUsuario(db.Model):
    __tablename__ = 'adm_roles_usuario'

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey(
        'adm_usuarios.id'), nullable=False)
    rol = db.Column(db.String(50), db.ForeignKey(
        'adm_roles.rol'), default=None)
    usuario_creacion_id = db.Column(db.Integer, default=None)
    fecha_creacion = db.Column(
        db.DateTime(), default=None)
    usuario_modificacion_id = db.Column(db.Integer, default=None)
    fecha_modificacion = db.Column(
        db.DateTime(), default=None)
    activo = db.Column(db.Boolean(4), default=None)
    propietario_id = db.Column(db.Integer, default=None)


class AdmUsuarioPersona(db.Model):
    __tablename__ = 'adm_usuario_persona'

    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    persona_id = db.Column(db.Integer, db.ForeignKey(
        'adm_personas.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey(
        'adm_usuarios.id'), nullable=False)


class Color(db.Model):
    __tablename__ = 'cat_colores'
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)

    descripcion = db.Column(db.String(250), nullable=False)
    activo = db.Column(db.Boolean(), nullable=False, default=b'1')
    usuario_creacion_id = db.Column(db.Integer, nullable=False, default=1)
    fecha_creacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    usuario_modificacion_id = db.Column(db.Integer, nullable=False, default=1)
    fecha_modificacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    propietario_id = db.Column(db.Integer, default=None)


class Destino(db.Model):
    __tablename__ = 'cat_destinos'

    id = db.Column(db.Integer, nullable=False,
                   primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(250), nullable=False)
    activo = db.Column(db.Boolean(), nullable=False, default=b'1')
    usuario_creacion_id = db.Column(db.Integer, nullable=False, default=1)
    fecha_creacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.now)
    usuario_modificacion_id = db.Column(db.Integer, nullable=False, default=1)
    fecha_modificacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.now)
    propietario_id = db.Column(db.Integer)


class DiagnosticoPalpado(db.Model):
    __tablename__ = 'cat_diagnosticos_palpado'

    id = db.Column(db.Integer, nullable=False,
                   primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(150), default=None)
    activo = db.Column(db.Integer, default=None)
    es_valor_reservado = db.Column(db.Integer, default=None)
    usuario_creacion_id = db.Column(db.String(45), default=None)
    fecha_creacion = db.Column(db.Integer, default=None)
    usuario_modificacion_id = db.Column(db.Integer, default=None)
    fecha_modificacion = db.Column(db.DateTime(), default=None)
    propietario_id = db.Column(db.Integer, default=None)


class Pais(db.Model):
    __tablename__ = 'cat_paises'

    id = db.Column(db.Integer, nullable=False,
                   autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    abreviatura = db.Column(db.String(5), nullable=False)

    estado = db.relationship('Estado')
    rancho = db.relationship('Rancho')


class Estado(db.Model):
    __tablename__ = 'cat_estados'

    id = db.Column(db.Integer, nullable=False,
                   autoincrement=True, primary_key=True)
    desc_estado = db.Column(db.String(250), nullable=False)
    pais_id = db.Column(db.Integer, db.ForeignKey(
        'cat_paises.id'), default=None)

    municipio = db.relationship('Municipio')
    localidad = db.relationship('Localidad')
    rancho = db.relationship('Rancho')
    persona = db.relationship('AdmPersona')


class Municipio(db.Model):
    __tablename__ = 'cat_municipios'

    id = db.Column(db.Integer, nullable=False,
                   autoincrement=True, primary_key=True)
    desc_municipio = db.Column(db.String(200), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey(
        'cat_estados.id'), default=None)

    localidad = db.relationship('Localidad')
    rancho = db.relationship('Rancho')


class Localidad(db.Model):
    __tablename__ = 'cat_localidades'

    id = db.Column(db.Integer, nullable=False,
                   autoincrement=True, primary_key=True)
    desc_localidad = db.Column(db.String(200), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey(
        'cat_estados.id'), default=None)
    municipio_id = db.Column(db.Integer, db.ForeignKey(
        'cat_municipios.id'), default=None)

    rancho = db.relationship('Rancho')


class Rancho(db.Model):
    __tablename__ = 'cat_ranchos'

    id = db.Column(db.Integer, nullable=False,
                   autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(50), default=None)
    ciudad = db.Column(db.String(50), default=None)
    telefono = db.Column(db.String(12), default=None)
    estado_id = db.Column(db.Integer, db.ForeignKey(
        'cat_estados.id'), default=None)
    municipio_id = db.Column(db.Integer, db.ForeignKey(
        'cat_municipios.id'), default=None)
    localidad_id = db.Column(db.Integer, db.ForeignKey(
        'cat_localidades.id'), default=None)
    pais_id = db.Column(db.Integer, db.ForeignKey(
        'cat_paises.id'), default=None)
    rfc = db.Column(db.String(18), default=None)
    email = db.Column(db.String(75), default=None)
    propietario_id = db.Column(
        db.Integer, db.ForeignKey('adm_propietarios.id'), default=None)
    como_llegar = db.Column(db.Text, nullable=False)
    activo = db.Column(db.Boolean(), nullable=False, default=b'1')
    usuario_creacion_id = db.Column(db.Integer, nullable=True, default=1)
    fecha_creacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    usuario_modificacion_id = db.Column(db.Integer, nullable=False, default=1)
    fecha_modificacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.utcnow)

    potrero = db.relationship('Potrero')
    lote = db.relationship('Lote')


class Potrero(db.Model):
    __tablename__ = 'cat_potreros'

    id = db.Column(db.Integer, nullable=False,
                   autoincrement=True, primary_key=True)
    rancho_id = db.Column(db.Integer, db.ForeignKey(
        'cat_ranchos.id'), nullable=False, default=0)
    nombre = db.Column(db.String(75), default=None)
    extension = db.Column(db.Numeric(10, 2), default=None)
    activo = db.Column(db.Boolean(), nullable=False, default=b'1')
    usuario_creacion_id = db.Column(
        db.Integer, nullable=False, default=1)
    fecha_creacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    usuario_modificacion_id = db.Column(db.Integer, nullable=False, default=1)
    fecha_modificacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    propietario_id = db.Column(
        db.Integer, default=None)

    lote = db.relationship('Lote')


class Lote(db.Model):
    __tablename__ = 'cat_lotes'

    id = db.Column(db.Integer, nullable=False,
                   autoincrement=True, primary_key=True)
    rancho_id = db.Column(db.Integer, db.ForeignKey(
        'cat_ranchos.id'), nullable=False)
    potrero_id = db.Column(db.Integer, db.ForeignKey(
        'cat_potreros.id'), nullable=False)
    nombre = db.Column(db.String(75), nullable=False)
    activo = db.Column(db.Boolean(), nullable=False, default=b'1')
    usuario_creacion_id = db.Column(
        db.Integer, nullable=False, default=1)
    fecha_creacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    usuario_modificacion_id = db.Column(db.Integer, nullable=False, default=1)
    fecha_modificacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    propietario_id = db.Column(
        db.Integer, default=None)


class Raza(db.Model):
    __tablename__ = 'cat_razas'

    id = db.Column(db.Integer, nullable=False,
                   autoincrement=True, primary_key=True)
    descripcion = db.Column(db.String(75), default=None)
    activo = db.Column(db.Boolean(), nullable=False, default=b'1')
    usuario_creacion_id = db.Column(
        db.Integer, nullable=False, default=1)
    fecha_creacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    usuario_modificacion_id = db.Column(db.Integer, nullable=False, default=1)
    fecha_modificacion = db.Column(
        db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    propietario_id = db.Column(
        db.Integer, default=None)


class TipoMovimiento(db.Model):
    __tablename__ = 'cat_tipo_movimientos'

    id = db.Column(db.Integer, nullable=False,
                   autoincrement=True, primary_key=True)
    descripcion = db.Column(db.String(150), nullable=False)


if __name__ == '__main__':
    manager.run()
