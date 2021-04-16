from flask import Flask, jsonify
from backend.account.login import *
from backend.items import *
from backend.models import *
from flask_cors import CORS
from database import *
import backend.database_script as script

app = Flask(__name__)
CORS(app)
app.register_blueprint(login_blueprint)
app.register_blueprint(item_blueprint)

# Create a database with the correct models.
Base.metadata.create_all(database.postgres_engine)

@app.route('/')
def hello_world():
  return jsonify(['Item A', 'Item B', 'Item C'])


if __name__ == '__main__':
  app.run()
