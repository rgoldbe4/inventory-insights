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
    recList = {}
    for item in categoryItems:
        if cart.items.count(item) > 1:
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
            if categoryItems.count(item) > 0:
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
    for item in cart.items:
        print(item.name)
    print("_______________")
    for item in evList:
        print(item.name)

    
    



