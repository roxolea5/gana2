from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

from controllers.razas import RazaController

razas_api = Blueprint('razas_api', __name__)


@ razas_api.route("/api/cat/razas")
@ jwt_required
def index():
    # return "Razas"
    results = [result.to_dict() for result in RazaController.get_all()]

    return jsonify(results)
