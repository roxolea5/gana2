from models.cat_paises import Pais


class PaisController:

    @staticmethod
    def get_all():
        # return results
        return Pais.query.filter().all()
