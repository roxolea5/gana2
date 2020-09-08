from models.adm_roles import Rol


class RolController:

    @staticmethod
    def get_all():
        # return results
        return Rol.query.filter().all()
