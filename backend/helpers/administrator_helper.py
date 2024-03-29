from database import *
from backend.models import *

def add(session, license, first_name, last_name, email, owner, password):
  administrator = Administrator(license=license, first_name=first_name, last_name=last_name,
                                email=email, owner=owner, password=password)
  session.add(administrator)
  session.commit()
  session.refresh(administrator)
  return administrator

# Get all Administrators from a license.
def get_by_license(session, license):
  return session.query(Administrator).filter_by(license=license).all()

def get(session, id):
  return session.query(Administrator).filter_by(id=id).first()

def delete(session, id):
  admin = get(id)
  if admin is not None:
    session.delete(admin)
    session.commit()
    return True
  return False

def login(session, email, password):
  return session.query(Administrator).filter_by(email=email, password=password).first()
