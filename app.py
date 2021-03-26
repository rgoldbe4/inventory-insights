import hashlib

from flask import Flask, jsonify
import database
from models import *

app = Flask(__name__)

# Create a database with the correct models.
database.Base.metadata.create_all(database.postgres_engine)


@app.route('/')
def hello_world():
  return jsonify()


if __name__ == '__main__':
  app.run()
