from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.colores import ColorController

colores_api = Blueprint('colores_api', __name__)


@colores_api.route("/api/cat/colores")
def index():
    # return "Colores"
    results = [result.to_dict() for result in ColorController.get_all()]

    return jsonify(results)
