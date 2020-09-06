from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect

razas_api = Blueprint('razas_api', __name__)


@razas_api.route("/razas")
def razas():
    return "Razas"
