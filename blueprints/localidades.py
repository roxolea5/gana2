from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect, make_response
from controllers.localidades import LocalidadController

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
        print(str(e))

    return response
