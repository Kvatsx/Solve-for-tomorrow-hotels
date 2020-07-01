from flask import Blueprint, jsonify, request, render_template
from flask_cors import CORS

mod = Blueprint('main', __name__)
CORS(mod)

@mod.route('/', methods=['GET'])
def index():
    """Landing page"""
    return render_template('home.html')
