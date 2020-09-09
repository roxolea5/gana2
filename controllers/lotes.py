from models.cat_lotes import Lote


class LoteController:

    @staticmethod
    def get_all():
        # return results
        return Lote.query.filter().all()
