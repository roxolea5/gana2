from models.cat_localidades import Localidad
from extensions.db import DB
db = DB.db


class LocalidadLogic:

    def __init__(self):
        pass

    @staticmethod
    def findLocalidadByName(desc_localidad):
        return Localidad.query.filter_by(desc_localidad=desc_localidad).first()

    @staticmethod
    def create(desc_localidad, estado_id, municipio_id):
        localidad = Localidad(dict({
            "desc_localidad": desc_localidad,
            "estado_id": estado_id,
            "municipio_id": municipio_id
        }))

        db.session.add(localidad)

        db.session.commit()
        return localidad
