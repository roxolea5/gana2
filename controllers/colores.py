from models.cat_colores import Color


class ColorController:

    @staticmethod
    def get_all():
        # return results
        return Color.query.filter().all()
