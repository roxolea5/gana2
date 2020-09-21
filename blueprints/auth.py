from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect, make_response
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_raw_jwt
)
from datetime import timedelta

from controllers.auth import AuthController

auth_api = Blueprint('auth_api', __name__)


@auth_api.route('/health', methods=['GET'])
# @cross_origin()
def health():
    print("Server is working!")
    return jsonify("Health is ok!"), 200


@auth_api.route("/login")
def login():

    username = "roxana"
    password = "roxana5"

    try:
        user = AuthController.verify_user_for_jwt(username, password)
    except Exception as e:
        # logger.error("File: [{script}]".format(
        #     script="/".join(__file__.split('/')[-2:])))
        # logger.error(str(e))
        return jsonify("Unauthorized"), 503

    if user:
        # expires = timedelta(seconds=15)
        expires = timedelta(days=2)
        access_token = create_access_token(
            identity=username, expires_delta=expires)
        # return jsonify(access_token=access_token), 200
        results = jsonify(access_token=access_token)
        return make_response(results, 200)

    return jsonify("Unauthorized"), 401
