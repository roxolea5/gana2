from flask import Blueprint, jsonify, render_template, request, send_from_directory, session, redirect

web_api = Blueprint('web_api', __name__)


@web_api.route('/')
def index():
    # return render_template('index.html')
    return "Hi"
