from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.potreros import PotreroController

potreros_api = Blueprint('potreros_api', __name__)


@potreros_api.route("/api/cat/potreros")
def index():
    # return "Potreros"
    results = [result.to_dict() for result in PotreroController.get_all()]

    return jsonify(results)
