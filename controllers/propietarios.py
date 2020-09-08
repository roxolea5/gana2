from models.adm_propietarios import Propietario


class PropietarioController:

    @staticmethod
    def get_all():
        # return results
        return Propietario.query.filter().all()
