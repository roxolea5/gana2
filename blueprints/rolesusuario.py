from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.rolesusuario import RolUsuarioController

roles_usuario_api = Blueprint('roles_usuario_api', __name__)


@roles_usuario_api.route("/api/adm/roles/usuario")
def index():
    # return "RolesUsuario"
    results = [result.to_dict() for result in RolUsuarioController.get_all()]

    return jsonify(results)
