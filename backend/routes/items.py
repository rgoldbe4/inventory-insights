from flask import Blueprint, render_template, abort, jsonify, request
from flask.json import dumps

from backend.models import Item
from database import *
from backend.helpers import user_helper, license_helper, cart_helper, item_helper
from backend import graphs

item_blueprint = Blueprint('item_blueprint', __name__)


@item_blueprint.route('/items/all', methods=['POST'])
def get_all_items():
  data = request.json
  license_id = data['license_id']
  session = Session()
  license = license_helper.get(session=session, id=license_id)
  all_items = item_helper.get_by_license(session=session, license=license)
  items = [item.to_dict() for item in all_items]
  session.close()
  return jsonify({ 'items' : items })


@item_blueprint.route('/items/item', methods=['POST'])
def get_item():
  data = request.json
  item_id = data['id']
  session = Session()
  item = item_helper.get(session, item_id)
  item = item.to_dict()
  session.close()
  return jsonify({ 'item' : item })


@item_blueprint.route('/items/addItem', methods=['POST'])
def add_item():
  data = request.json
  new_item = data['item']
  license_id = data['license_id']
  session = Session()

  name = new_item['name']
  cost = new_item['cost']
  price = new_item['price']
  description = new_item['description']
  instock = new_item['instock']
  category = new_item['category']
  license = license_helper.get(session, license_id)
  item = item_helper.add(session=session, cost=cost, price=price, description=description, instock=instock, name=name, category=category, license=license)
  item = item.to_dict()

  session.close()

  return jsonify({ 'item' : item })


@item_blueprint.route('/items/discontinue', methods=['POST'])
def discontinue():
  data = request.json
  item_id = data['id']
  license_id = data['license_id']
  session = Session()
  item = item_helper.discontinue(session=session, id=item_id)
  item = item.to_dict()
  session.close()
  return jsonify({ 'item': item })


@item_blueprint.route('/items/save', methods=['POST'])
def save():
  data = request.json
  updated_item = data['item']
  result = False
  session = Session()
  # Only editable fields: cost, price, description, instock, name
  item = item_helper.get(session=session, id=updated_item['id'])
  item.cost = updated_item['cost']
  item.price = updated_item['price']
  item.description = updated_item['description']
  item.instock = updated_item['instock']
  item.name = updated_item['name']
  session.commit()
  item = item.to_dict()
  session.close()
  return jsonify({ 'item': item, 'result': True })

@item_blueprint.route('/items/monthlySales', methods=['POST'])
def salesGraph():
  data = request.json
  item_id = data['item_id']
  session = Session()
  sales = graphs.monthlySales(session, item_id)
  print(sales)
  session.close()
  return jsonify({ 'sales': sales })





