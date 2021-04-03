from backend.models import *
from database import *
import hashlib


def testDatabase():
  session = Session()
  # Test License
  # This works, so just grab a random license lol
  license = session.query(License).filter_by(id=1).first()
  print("Accounts:", license.accounts)

  # Test administrators
  # Administrators are required to have a License
  encrypted_password = hashlib.sha256("password".encode()).digest()
  admin = session.query(Administrator).filter_by(id=1).first()
  print("Administrator:", admin.first_name, admin.last_name)

  # Test User
  # Users can be created without a License
  user_a = User(email="user@email.com", password=encrypted_password,
               first_name="UserA", last_name="Last")
  user_b = User(email="userB@email.com", password=encrypted_password,
               first_name="UserB", last_name="Last")
  session.add(user_a)
  session.add(user_b)
  session.commit()

  # Test Item

  # Test Cart

  # Test Order


  session.close()
