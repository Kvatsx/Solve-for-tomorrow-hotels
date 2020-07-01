from flask import Blueprint, jsonify, request
from flask_cors import CORS

mod = Blueprint('main', __name__)
CORS(mod)

@mod.route('/', methods=['GET'])
def index():
    return "Hello World!", 201
