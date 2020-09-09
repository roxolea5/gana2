from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.municipios import MunicipioController

municipios_api = Blueprint('municipios_api', __name__)


@municipios_api.route("/api/cat/municipios")
def index():
    # return "Municipios"
    results = [result.to_dict() for result in MunicipioController.get_all()]

    return jsonify(results)
