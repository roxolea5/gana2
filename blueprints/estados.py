from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.estados import EstadoController

estados_api = Blueprint('estados_api', __name__)


@estados_api.route("/api/cat/estados")
def index():
    # return "Estados"
    results = [result.to_dict() for result in EstadoController.get_all()]

    return jsonify(results)
