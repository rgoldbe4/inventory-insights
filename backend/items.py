from flask import Blueprint, render_template, abort, jsonify, request
from flask.json import dumps

from backend.models import Item
from database import *
from backend.helpers import user_helper, license_helper, cart_helper, item_helper

item_blueprint = Blueprint('item_blueprint', __name__)


@item_blueprint.route('/items/all')
def get_all_items():
  session = Session()
  all_items = session.query(Item).all()
  items = [item.to_dict() for item in all_items]
  session.close()
  return jsonify({ 'items' : items })


@item_blueprint.route('/items/item', methods=['POST'])
def get_item():
  data = request.json
  item_id = data['id']
  session = Session()
  item = item_helper.get(session, item_id)
  item = item.serialize()
  session.close()
  return jsonify({ 'item' : item })

