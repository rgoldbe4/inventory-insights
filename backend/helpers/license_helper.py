from database import *
from backend.models import *

def add(session, accounts):
  license = License(accounts=accounts)
  session.add(license)
  session.commit()
  session.refresh(license)
  return license


def get(session, id):
  return session.query(License).filter_by(id=id).first()

def delete(session, id):
  license = get(id)
  if license is not None:
    session.delete(license)
    session.commit()
    return True
  return False
