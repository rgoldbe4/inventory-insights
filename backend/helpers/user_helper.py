from database import *
from backend.models import *

"""
add_user
Creates a User in the database
Returns the completed User
"""
def add(session, first_name, last_name, email, password):
  user = User(first_name=first_name, last_name=last_name, email=email, password=password)
  session.add(user)
  session.commit()
  session.refresh(user)
  return user

"""
get_user
Obtain a User from the database
Returns the user, can be None.
"""
def get(session, id):
    return session.query(User).filter_by(id=id).first()

def get_login(session, email, password):
  return session.query(User).filter_by(email=email, password=password).first()


"""
delete_user
Finds user by email (username) and password
Returns boolean depending if entity exists
"""
def delete(session, id):
  user = get(session=session, id=id)
  if user is not None:
    session.delete(user)
    session.commit()
    return True
  return False
