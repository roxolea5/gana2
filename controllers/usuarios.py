from models.usuarios import Usuario


class UsuarioController:

    @staticmethod
    def get_all():
        # return results
        return Usuario.query.filter().all()
