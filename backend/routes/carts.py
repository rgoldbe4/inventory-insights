from flask import jsonify, request, Blueprint

from backend.helpers import cart_helper, user_helper, item_helper
from database import Session

cart_blueprint = Blueprint('cart_blueprint', __name__)

@cart_blueprint.route('/cart', methods=['POST'])
def get_cart():
  data = request.json
  cart_id = data['id']
  session = Session()
  cart = cart_helper.get(session, cart_id)
  cart = cart.to_dict()
  session.close()
  return jsonify({ 'cart': cart })
