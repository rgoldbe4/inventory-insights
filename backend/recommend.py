from backend.models import *
import random


def recommendItem(session, cart):
    price = 0
    meid = 0
    items = cart.items
    for item in items:
        if item.price > price:
            price = item.price
            meid = item.id
    meitem = session.query(Item).filter_by(id = meid).one()
    category = meitem.category
    categoryItems = session.query(Item).filter_by(category = category).all()
    allItems = session.query(Item).all()
    evList = {}
    recList = []
    for item in categoryItems:
        occurences = len(session.query(association_cart_table).filter_by(item_id = item.id, cart_id = cart.id).all())
        if occurences == 0:
            recs = session.query(Recommendation).filter_by(recommended = item).all()
            suc = 0
            total = 0
            if len(recs) > 0:
                for rec in recs:
                    if rec.success:
                        suc += 1
                    total += 1
                profit = item.price - item.cost
                ev = (profit*suc)/total
                evList[item] = ev
    for item in allItems:
        if len(evList) < 2:
            if item.category != category:
                occurences = len(session.query(association_cart_table).filter_by(item_id = item.id, cart_id = cart.id).all())
                if occurences == 0:
                    recs = session.query(Recommendation).filter_by(recommended = item).all()
                    suc = 0
                    total = 0
                    if len(recs) > 0:
                        for rec in recs:
                            if rec.success:
                                suc += 1
                            total += 1
                        profit = item.price - item.cost
                        ev = (profit*suc)/total
                        evList[item] = ev
        else:
            break
    evList = sorted(evList, key = evList.get)
    recList.append(evList[0])
    recList.append(evList[1])
    return recList
    
    



