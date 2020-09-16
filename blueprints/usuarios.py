from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.usuarios import UsuarioController

usuarios_api = Blueprint('usuarios_api', __name__)


@usuarios_api.route("/api/usuarios")
def index():
    # return "Usuarios"
    results = [result.to_dict() for result in UsuarioController.get_all()]

    return jsonify(results)
