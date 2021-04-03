import os
from datetime import date
import database

from sqlalchemy.orm.exc import NoResultFound
from werkzeug.utils import secure_filename
from models import *

def addItem(session,name,price,category):
    session.add(Item(name = name, price = price, category = category))
    session.commit()

def getItem(session, note_id):
    ouritem = session.query(Item).filter_by(id=note_id).first()
    return ouritem

def editItem(session, note_id, name, price, category):
    ouritem = getItem(session, note_id)
    ouritem.name = name
    ouritem.price = price
    ouritem.category = category

def deleteItem(session, note_id):
    ouritem = getItem(session, note_id)
    session.delete(ouritem)
    session.commit()

    

