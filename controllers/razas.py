from models.cat_razas import Raza


class RazaController:

    @staticmethod
    def get_all():
        # return results
        return Raza.query.filter().all()
