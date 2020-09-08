from models.cat_diagnosticos_palpado import DiagnosticoPalpado


class DiagnosticoPalpadoController:

    @staticmethod
    def get_all():
        # return results
        return DiagnosticoPalpado.query.filter().all()
