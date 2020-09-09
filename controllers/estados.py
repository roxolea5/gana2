from models.cat_estados import Estado


class EstadoController:

    @staticmethod
    def get_all():
        # return results
        return Estado.query.filter().all()
