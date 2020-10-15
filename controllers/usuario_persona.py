from models.adm_usuario_persona import UsuarioPersona


class UsuarioPersonaController:

    @staticmethod
    def get_all():
        # return results
        return UsuarioPersona.query.filter().all()
