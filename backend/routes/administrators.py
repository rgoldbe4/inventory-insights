from flask import Blueprint, jsonify, request
from database import *
from backend.helpers import administrator_helper, license_helper

administrator_blueprint = Blueprint('administrator_blueprint', __name__)


@administrator_blueprint.route('/admin/login', methods=['POST'])
def login():
  req = request.json
  email = req['email']
  password = req['encrypted_password']  # Comes encrypted
  session = Session()
  # Grab the current administrator from the database, if it exists it will return "None".
  admin = administrator_helper.login(session=session, email=email, password=password)
  exists = True
  admin_result = None
  admin_license = None

  # Check if the login credentials worked
  if admin is None:
    exists = False
  else:
    # Serialize the admin variable from SQLAlchemy object
    admin_result = admin.to_dict()
    admin_license = admin.license.to_dict()


  # Close the session to the database.
  session.close()
  return jsonify({ 'exists': exists, 'administrator': admin_result, 'license': admin_license })


@administrator_blueprint.route('/admin/register', methods=['POST'])
def create():
  req = request.json
  print(req)

  first_name = req['first_name']
  last_name = req['last_name']
  email = req['email']
  password = req['password'] # This should come encrypted.
  license_id = req['license']


  # Check if user exists
  session = Session()
  admin = administrator_helper.login(session=session, email=email, password=password)
  admin_license = license_helper.get(session=session, id=license_id)
  errors = []

  if admin is None:
    # Ensure that they have not used up their license.
    administrators = administrator_helper.get_by_license(session=session, license=admin_license)
    if admin_license.accounts > len(administrators):
      # Add administrator to database.
      admin = administrator_helper.add(session=session, first_name=first_name, last_name=last_name,
                                     email=email, password=password, license=admin_license, owner=False)
    else:
      errors.append("This license has no more remaining Administrator accounts left.")
  else:
    errors.append("The administrator already exists. Cannot create duplicates.")

  admin = admin.to_dict()
  admin_license = admin_license.to_dict()
  session.close()
  return jsonify({ 'administrator': admin, 'license': admin_license, 'errors': errors })

# Receives a license id and returns all administrators.
@administrator_blueprint.route('/admin/all', methods=['POST'])
def get_all_admins():
  # Recode so it returns all admins from a license.
  data = request.json
  license_id = data['id']
  session = Session()
  admin_license = license_helper.get(session, license_id)
  administrators = administrator_helper.get_by_license(session, admin_license)
  admins = [admin.to_dict() for admin in administrators]
  license = admin_license.to_dict()
  return jsonify({ 'administrators': admins, 'license': license })

# When we call this route, given an ID, we we will return the Administrator of that ID
@administrator_blueprint.route('/admin', methods=['POST'])
def get_single_admin():
  data = request.json
  # Get the ID from the POST data
  admin_id = data['id']

  # Grab the ID of the administrator
  session = Session() # Creates a session that connects to the database
  admin = administrator_helper.get(session=session, id=admin_id)
  if admin is not None:
    admin = admin.to_dict() # Serializes the data so it can be converted to JSON

  # Return the administrator
  return jsonify({ 'admin': admin })


@administrator_blueprint.route('/admin/save', methods=['POST'])
def save_admin():
  data = request.json
  admin_id = data['id']
  first_name = data['first_name']
  last_name = data['last_name']
  email = data['email']

  session = Session()
  admin = administrator_helper.get(session, admin_id)
  admin.first_name = first_name
  admin.last_name = last_name
  admin.email = email

  session.commit()
  admin = admin.to_dict()
  session.close()
  return jsonify({ 'admin': admin })
