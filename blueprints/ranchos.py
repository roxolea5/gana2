from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.ranchos import RanchoController

ranchos_api = Blueprint('ranchos_api', __name__)


@ranchos_api.route("/api/cat/ranchos")
def index():
    # return "Ranchos"
    results = [result.to_dict() for result in RanchoController.get_all()]

    return jsonify(results)
