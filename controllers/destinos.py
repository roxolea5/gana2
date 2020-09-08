from models.cat_destinos import Destino


class DestinoController:

    @staticmethod
    def get_all():
        # return results
        return Destino.query.filter().all()
