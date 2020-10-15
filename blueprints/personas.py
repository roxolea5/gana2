from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.personas import PersonaController

personas_api = Blueprint('personas_api', __name__)


@personas_api.route("/api/adm/personas")
def index():
    # return "Personas"
    results = [result.to_dict() for result in PersonaController.get_all()]

    return jsonify(results)
