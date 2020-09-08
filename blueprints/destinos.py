from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.destinos import DestinoController

destinos_api = Blueprint('destinos_api', __name__)


@destinos_api.route("/api/cat/destinos")
def index():
    # return "Destinos"
    results = [result.to_dict() for result in DestinoController.get_all()]

    return jsonify(results)
