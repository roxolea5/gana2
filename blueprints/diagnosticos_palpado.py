from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.diagnosticos_palpado import DiagnosticoPalpadoController

diagnosticos_palpado_api = Blueprint('diagnosticos_palpado_api', __name__)


@diagnosticos_palpado_api.route("/api/cat/diagnosticos_palpado")
def index():
    # return "Diagnosticos Palpado"
    results = [result.to_dict()
               for result in DiagnosticoPalpadoController.get_all()]

    return jsonify(results)
