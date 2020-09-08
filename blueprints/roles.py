from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.roles import RolController

roles_api = Blueprint('roles_api', __name__)


@roles_api.route("/api/adm/roles")
def index():
    # return "Roles"
    results = [result.to_dict() for result in RolController.get_all()]

    return jsonify(results)
