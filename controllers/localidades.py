from models.cat_localidades import Localidad


class LocalidadController:

    @staticmethod
    def get_all():
        # return results
        return Localidad.query.filter().all()
