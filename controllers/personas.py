from models.adm_personas import Persona


class PersonaController:

    @staticmethod
    def get_all():
        # return results
        return Persona.query.filter().all()
