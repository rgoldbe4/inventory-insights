from flask import jsonify, request, Blueprint

from backend.helpers import cart_helper, user_helper, item_helper
from backend.models import association_order_table
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

@cart_blueprint.route('/cart/item/add', methods=['POST'])
def add_item_to_cart():
  data = request.json
  item_id = data['item_id']
  cart_id = data['cart_id']

  session = Session()
  cart = cart_helper.get(session=session, id=cart_id)
  item = item_helper.get(session=session, id=item_id)
  cart.items.append(item)
  session.commit()
  session.close()

  return jsonify({ 'success': True })

@cart_blueprint.route('/cart/active', methods=['POST'])
def check_if_user_has_cart():
  data = request.json
  user_id = data['id']
  session = Session()

  user = user_helper.get(session=session, id=user_id)
  cart = None
  for c in user.carts:
    if c.active:
      cart = c

  # If cart doesn't exist, then create one with no items.
  if cart is None:
    cart = cart_helper.add(session=session, user=user, items=[], active=True)

  cart = cart.to_dict()
  session.close()

  return jsonify({ 'cart': cart })

@cart_blueprint.route('/cart/item/remove', methods=['POST'])
def remove_item_from_cart():
  data = request.json
  cart_id = data['cart_id']
  item_id = data['item_id']
  session = Session()
  # Find the cart
  cart = cart_helper.get(session=session, id=cart_id)
  item = item_helper.get(session=session, id=item_id)
  cart.items.remove(item)
  session.commit()
  session.refresh(cart)
  cart = cart.to_dict()
  item = item.to_dict()
  session.close()
  return jsonify({ 'cart': cart, 'item': item })
