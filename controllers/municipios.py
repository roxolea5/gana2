from models.cat_municipios import Municipio


class MunicipioController:

    @staticmethod
    def get_all():
        # return results
        return Municipio.query.filter().all()
