from backend.models import *

def add(session, user, items):
  order = Order(items=items)
  session.add(order)
  session.commit()
  session.refresh(order)
  user.orders.append(order)
  session.commit()
  return order

def get(session, id):
  return session.query(Order).filter_by(id=id).first()

def get_all_by_user(session, user_id):
  return session.query(Order).filter_by(id=id).all()

def get_all(session):
  return session.query(Order).all()

def delete(session, id):
  order = get(id)
  if order is not None:
    session.delete(order)
    session.commit()
    return True
  return False
