from flask import Blueprint, jsonify, request
from database import *
from backend.helpers import user_helper

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/user', methods=['POST'])
def get_user():
  data = request.json
  user_id = data['id']

  session = Session()
  user = user_helper.get(session, user_id)
  if user is not None:
    user = user.to_dict()

  session.close()
  return jsonify({ 'user': user })

@user_blueprint.route('/user/login', methods=['POST'])
def login():
  data = request.json
  errors = []
  email = data['email']
  password = data['encrypted_password']
  session = Session()
  user = user_helper.get_login(session=session, email=email, password=password)
  if user is not None:
    user = user.to_dict()
  else:
    errors.append('User is not found. Try another combination.')
  session.close()
  return jsonify({ 'user': user, 'errors': errors })

@user_blueprint.route('/user/register', methods=['POST'])
def register():
  data = request.json
  errors = []
  # Registration POST information
  email = data['email']
  first_name = data['first_name']
  last_name = data['last_name']
  password = data['encrypted_password']

  session = Session()
  # Determine if the user already exists.
  user = user_helper.get_login(session=session, email=email, password=password)
  if user is None:
    user = user_helper.add(session=session, first_name=first_name, last_name=last_name, email=email, password=password)
    user = user.to_dict()
  else:
    errors.append("That email is already in use. Try another.")

  session.close()
  return jsonify({ 'errors': errors, 'user': user })

@user_blueprint.route('/user/save', methods=['POST'])
def save_user():
  data = request.json
  user_id = data['id']
  first_name = data['first_name']
  last_name = data['last_name']
  email = data['email']

  session = Session()
  user = user_helper.get(session, user_id)
  user.first_name = first_name
  user.last_name = last_name
  user.email = email

  session.commit()
  user = user.to_dict()
  session.close()
  return jsonify({ 'user': user })
