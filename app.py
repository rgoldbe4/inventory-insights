import hashlib

from flask import Flask, jsonify
import database
from models import *

app = Flask(__name__)

# Create a database with the correct models.
database.Base.metadata.create_all(database.postgres_engine)

session = database.Session()
license = session.query(License).filter_by(id=1).first()
password = hashlib.sha256("password1".encode()).digest()
admins = license.administrators

admin = session.query(Administrator).filter_by(id=2).first()

print(admin.first_name, admin.license.accounts)

session.commit()
session.close()


@app.route('/')
def hello_world():
  return jsonify()


if __name__ == '__main__':
  app.run()
