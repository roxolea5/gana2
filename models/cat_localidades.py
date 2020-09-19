from sqlalchemy_serializer import SerializerMixin
from extensions.db import DB
db = DB.db
DB_ENGINE = 'dev'


class Localidad(db.Model, SerializerMixin):
    # __bind_key__ = DB_ENGINE
    __tablename__ = 'cat_localidades'
    """
    __table_args__ = {
        'autoload': True,
        'autoload_with': DB.engines[DB_ENGINE].engine
    }
    """
    id = db.Column(db.Integer, nullable=False,
                   autoincrement=True, primary_key=True)
    desc_localidad = db.Column(db.String(200), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey(
        'cat_estados.id'), default=None)
    municipio_id = db.Column(db.Integer, db.ForeignKey(
        'cat_municipios.id'), default=None)

    def __init__(self, localidad):
        self.id = localidad.get("id", None)
        self.desc_localidad = localidad.get("desc_localidad")
        self.estado_id = localidad.get("estado_id")
        self.municipio_id = localidad.get("municipio_id")
