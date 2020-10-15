from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.usuario_persona import UsuarioPersonaController

usuario_persona_api = Blueprint('usuario_persona_api', __name__)


@usuario_persona_api.route("/api/adm/usuario/persona")
def index():
    # return "UsuarioPersona"
    results = [result.to_dict()
               for result in UsuarioPersonaController.get_all()]

    return jsonify(results)
