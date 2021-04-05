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


def delete(session, id):
  item = get(session=session, id=id)
  if item is not None:
    session.delete(item)
    session.commit()
    return True
  return False
