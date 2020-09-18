from models.cat_localidades import Localidad


class LocalidadController:

    @staticmethod
    def get_all():
        localidades = []
        try:
            for localidad in Localidad.query.filter().all():
                localidades.append(
                    dict({
                        "id": localidad.id,
                        "desc_localidad": localidad.desc_localidad,
                        "estado_id": localidad.estado_id,
                        "municipio_id": localidad.municipio_id
                    })
                )
        except Exception as e:
            print(str(e))

        return localidades  # Localidad.query.filter().all()

    @staticmethod
    def get_by_page(page_number):
        results = []
        try:
            localidades = Localidad.query.filter().paginate(page=page_number, per_page=10,
                                                            error_out=True, max_per_page=None)

            for localidad in localidades.items:
                results.append(
                    dict({
                        "id": localidad.id,
                        "desc_localidad": localidad.desc_localidad,
                        "estado_id": localidad.estado_id,
                        "municipio_id": localidad.municipio_id
                    })
                )
        except Exception as e:
            print(str(e))

        return results  # Localidad.query.filter().all()
