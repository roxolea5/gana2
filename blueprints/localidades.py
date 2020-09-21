from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect, make_response

from controllers.localidades import LocalidadController
from logic.localidadLogic import LocalidadLogic

localidades_api = Blueprint('localidades_api', __name__)


@localidades_api.route('/api/cat/localidades/', methods=['GET'])
def index():
    args = request.args

    if "page_number" in args:
        page_number = int(args['page_number'])
    else:
        page_number = 1

    try:
        # return "Localidades"
        # results = [result.to_dict() for result in LocalidadController.get_all()]
        results = LocalidadController.get_by_page(page_number)
        response = make_response(jsonify(results), 200)
    except Exception as e:
        response = make_response(jsonify(str(e)))

    return response


@ localidades_api.route('/api/cat/localidades/create', methods=['POST'])
def create():
    desc_localidad = request.form['desc_localidad']
    estado_id = request.form['estado_id']
    municipio_id = request.form['municipio_id']

    localidad = LocalidadLogic.findLocalidadByName(desc_localidad)

    if localidad is not None:
        response = make_response(jsonify("Localidad Duplicada"), 409)
    else:
        try:
            localidad = LocalidadLogic.create(
                desc_localidad, estado_id, municipio_id)
            response = make_response("Localidad creada", 200)
        except Exception as e:

            response = make_response(jsonify(str(e)))

    return response
