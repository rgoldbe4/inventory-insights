from backend.models import *

def add(session, user, items):
  cart = Cart(user=user, items=items)
  session.add(cart)
  session.commit()
  session.refresh(cart)
  return cart


def get(session, id):
  return session.query(Cart).filter_by(id=id).first()


def delete(session, id):
  cart = get(session=session, id=id)
  if cart is not None:
    session.delete(cart)
    session.commit()
    return True
  return False
