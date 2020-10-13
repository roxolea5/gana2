from models.adm_roles_usuario import RolUsuario


class RolUsuarioController:

    @staticmethod
    def get_all():
        # return results
        return RolUsuario.query.filter().all()
