
from flask import Blueprint, render_template, abort, jsonify, request
from flask.json import dumps

from database import *
from backend.helpers import user_helper, license_helper, cart_helper, administrator_helper

login_blueprint = Blueprint('login_blueprint', __name__)


@login_blueprint.route('/account/login/', methods=['POST'])
def index():
  req = request.json
  email = req['email']
  password = req['password'] # Comes encrypted
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
  return jsonify({ 'exists': exists, 'administrator': admin })

# Registration
@login_blueprint.route('/account/create/', methods=['POST'])
def create():
  req = request.json
  first_name = req['first_name']
  last_name = req['last_name']
  email = req['email']
  password = req['password'] # This should come encrypted.
  license_id = req['license_id']

  # Check if user exists
  exists = True
  session = Session()
  admin = administrator_helper.get(session=session, email=email, password=password)
  admin_license = license_helper.get(session=session, id=license_id)
  message = ""

  if admin is None:
    exists = False
    # Ensure that they have not used up their license.
    if admin_license.accounts > len(admin_license.administrators):
      # Add administrator to database.
      admin = administrator_helper.add(session=session, first_name=first_name, last_name=last_name,
                                     email=email, password=password, license=admin_license)
      message = "Success. Administrator was successfully registered."
    else:
      message = "This license has no more remaining Administrator accounts left."
  else:
    message = "The administrator already exists. Cannot create duplicates."

  admin = admin.to_dict()
  session.close()
  return jsonify({ 'administrator': admin, 'exists': exists, 'message': message })
