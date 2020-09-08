from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect
from controllers.tipo_movimientos import TipoMovimientoController

tipo_movimientos_api = Blueprint('tipo_movimientos_api', __name__)


@tipo_movimientos_api.route("/api/cat/tipo_movimientos")
def index():
    # return "Tipo Movimientos"
    results = [result.to_dict()
               for result in TipoMovimientoController.get_all()]

    return jsonify(results)
