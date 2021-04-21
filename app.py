from flask import Flask

from backend.routes.administrators import administrator_blueprint
from backend.routes.items import *
from backend.models import *
from flask_cors import CORS
from database import *

app = Flask(__name__)
CORS(app)

app.register_blueprint(administrator_blueprint)
app.register_blueprint(item_blueprint)

# Create a database with the correct models.
Base.metadata.create_all(database.postgres_engine)

@app.route('/')
def hello_world():
  return jsonify(['Item A', 'Item B', 'Item C'])

if __name__ == '__main__':
  app.run()
