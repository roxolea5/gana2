from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.propietarios import PropietarioController

propietarios_api = Blueprint('propietarios_api', __name__)


@propietarios_api.route("/api/adm/propietarios")
def index():
    # return "Propietarios"
    results = [result.to_dict() for result in PropietarioController.get_all()]

    return jsonify(results)
