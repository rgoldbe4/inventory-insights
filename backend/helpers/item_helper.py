from database import *
from backend.models import *

def add(session, name, price):
  item = Item(price=price, name=name)
  session.add(item)
  session.commit()
  session.refresh(item)
  return item


def get(session, id):
  return session.query(Item).filter_by(id=id).first()

def get_by_license(session, license):
  return session.query(Item).filter_by(license=license).all()

def delete(session, id):
  item = get(session=session, id=id)
  if item is not None:
    session.delete(item)
    session.commit()
    return True
  return False

def discontinue(session, id):
  item = get(session=session, id=id)
  if item is not None:
    item.discontinued = True
    session.commit()
    session.refresh(item)
  return item
