
from flask import Blueprint, render_template, abort, jsonify, request
from flask.json import dumps

from database import *
from backend.helpers import user_helper, license_helper, cart_helper, administrator_helper

login_blueprint = Blueprint('login_blueprint', __name__)


@login_blueprint.route('/account/login/', methods=['POST'])
def index():
  req = request.json
  email = req['email']
  password = req['password']
  session = Session()
  # Grab the current administrator from the database, if it exists it will return "None".
  admin = administrator_helper.login(session=session, email=email, password=password)
  exists = True

  # Check if the login credentials worked
  if admin is None:
    exists = False
  else:
    # Serialize the admin variable from SQLAlchemy object
    admin = admin.to_dict()

  # Close the session to the database.
  session.close()
  return jsonify({'exists': exists, 'administrator': admin })

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

  cart = cart_helper.get(session, 1)
  session.close()
  return jsonify({ 'user': user })
