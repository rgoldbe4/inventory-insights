
from flask import Blueprint, render_template, abort, jsonify, request
from flask.json import dumps

from database import *
from backend.helpers import user_helper, license_helper, cart_helper

login_blueprint = Blueprint('login_blueprint', __name__)


@login_blueprint.route('/account/')
def index():
  return jsonify({'message': 'Hello World'})

@login_blueprint.route('/account/create/', methods=['POST'])
def create():
  req = request.json
  first_name = req['first_name']
  last_name = req['last_name']
  email = req['email']
  password = req['password']

  # Check if user exists
  session = Session()
  user = user_helper.get(session=session, email=email, password=password)
  if user is None:
    user = user_helper.add(session=session,
                                first_name=first_name,
                                last_name=last_name,
                                email=email,
                                password=password)

  cart = cart_helper.get(session, 1)
  session.close()
  return cart
