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
