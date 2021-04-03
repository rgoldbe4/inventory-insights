import hashlib

from flask import Flask, g, jsonify
import database
from models import *
from items import *
from licenses import *

app = Flask(__name__)

# Create a database with the correct models.
database.Base.metadata.create_all(database.postgres_engine)


@app.route('/')
def hello_world():
  newLicense(database.Session(), 30)
  newLicense(database.Session(), 50)
  
  print("______________________________________________________________")

  return jsonify()


if __name__ == '__main__':
  app.run()
