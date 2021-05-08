from flask import Blueprint, jsonify, request
from database import *
from backend.helpers import license_helper

license_blueprint = Blueprint('license_blueprint', __name__)

@license_blueprint.route('/license', methods=['POST'])
def get_license():
  data = request.json
  license_id = data['id']

  session = Session()
  license = license_helper.get(session, license_id)
  if license is not None:
    license = license.to_dict()

  session.close()
  return jsonify({ 'license': license })

@license_blueprint.route('/license/all', methods=['GET'])
def get_all_licenses():
  session = Session()
  licenses = license_helper.get_all(session)
  licenses = [l.to_dict() for l in licenses]
  session.close()
  return jsonify({ 'licenses': licenses })
