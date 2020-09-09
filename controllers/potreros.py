from models.cat_potreros import Potrero


class PotreroController:

    @staticmethod
    def get_all():
        # return results
        return Potrero.query.filter().all()
