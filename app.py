from flask import Flask

from backend.routes.administrators import administrator_blueprint
from backend.routes.carts import cart_blueprint
from backend.routes.orders import order_blueprint
from backend.routes.users import user_blueprint
from backend.routes.licenses import license_blueprint
from backend.routes.items import *
from backend.models import *
from flask_cors import CORS
from database import *

app = Flask(__name__)
CORS(app)

app.register_blueprint(administrator_blueprint)
app.register_blueprint(item_blueprint)
app.register_blueprint(cart_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(license_blueprint)
app.register_blueprint(order_blueprint)

# Create a database with the correct models.
Base.metadata.create_all(database.postgres_engine)

@app.route('/')
def hello_world():
  return jsonify(['Item A', 'Item B', 'Item C'])

if __name__ == '__main__':
  app.run()
