from models.cat_tipo_movimientos import TipoMovimiento


class TipoMovimientoController:

    @staticmethod
    def get_all():
        # return results
        return TipoMovimiento.query.filter().all()
