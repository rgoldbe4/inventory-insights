from flask import Blueprint, jsonify, request
from database import *
from backend.helpers import user_helper

order_blueprint = Blueprint('order_blueprint', __name__)

@order_blueprint.route('/orders', methods=['GET'])
def some_action():
  return jsonify({})
