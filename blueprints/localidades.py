from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.localidades import LocalidadController

localidades_api = Blueprint('localidades_api', __name__)


@localidades_api.route("/api/cat/localidades")
def index():
    # return "Localidades"
    results = [result.to_dict() for result in LocalidadController.get_all()]

    return jsonify(results)
