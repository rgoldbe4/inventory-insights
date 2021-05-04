from backend.models import *

def add(session, cart, recommended_item, success):
  recommend = Recommendation(cart=cart, recommended=recommended_item, success=success)
  session.add(recommend)
  session.commit()
  session.refresh(recommend)
  return recommend

def get(session, id):
  return session.query(Recommendation).filter_by(id=id).first()

def delete(session, id):
  recommendation = get(id)
  if recommendation is not None:
    session.delete(recommendation)
    session.commit()
    return True
  return False
