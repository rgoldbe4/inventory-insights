from flask import Blueprint, render_template, abort, jsonify

login_blueprint = Blueprint('login_blueprint', __name__)


@login_blueprint.route('/account/')
def index():
  return jsonify({'message': 'Hello World'})
