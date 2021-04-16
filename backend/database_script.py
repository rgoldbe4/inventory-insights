from backend.helpers import user_helper, item_helper, cart_helper, administrator_helper
from pprint import pprint
from backend.models import *
from database import *
import hashlib


def testDatabase():
  session = Session()
  # Test License
  # This works, so just grab a random license lol
  license = session.query(License).filter_by(id=1).first()

  # Test administrators
  # Administrators are required to have a License
  encrypted_password = hashlib.sha256("password".encode()).hexdigest()
  admin = administrator_helper.get(session, 1)

  # Test User
  # Users can be created without a License
  first_name = 'Ryan'
  last_name = 'Goldberg'
  email = 'admin@buffsovernexus.com'
  password = encrypted_password
  user = user_helper.get(session=session, email=email, password=password)

  # Test Item
  item_name = "Item Name"
  price = "2.50"
  item = item_helper.get(session, 1)
  item_b = item_helper.get(session, 2)
  items = [item, item_b]
  # Test Cart
  cart = cart_helper.get(session, 1)


  # Test Order


  session.close()
