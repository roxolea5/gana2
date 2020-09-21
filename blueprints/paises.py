from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.paises import PaisController

paises_api = Blueprint('paises_api', __name__)


@paises_api.route("/api/cat/paises")
def index():
    # return "Paises"
    results = [result.to_dict() for result in PaisController.get_all()]

    return jsonify(results)
