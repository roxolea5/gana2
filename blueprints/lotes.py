from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.lotes import LoteController

lotes_api = Blueprint('lotes_api', __name__)


@lotes_api.route("/api/cat/lotes")
def index():
    # return "Lotes"
    results = [result.to_dict() for result in LoteController.get_all()]

    return jsonify(results)
