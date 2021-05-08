from flask import Blueprint, jsonify, request
from database import *
from backend.helpers import user_helper, order_helper

order_blueprint = Blueprint('order_blueprint', __name__)

@order_blueprint.route('/orders/all', methods=['POST'])
def get_orders():
  data = request.json
  user_id = data['user_id']
  session = Session()
  user = user_helper.get(session=session, id=user_id)
  all_orders = order_helper.get_all(session=session, user_id=user)
  orders = [order.to_dict() for order in all_orders]
  session.close()
  return jsonify({'orders' : orders})


