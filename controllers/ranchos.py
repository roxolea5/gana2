from models.cat_ranchos import Rancho


class RanchoController:

    @staticmethod
    def get_all():
        # return results
        return Rancho.query.filter().all()
