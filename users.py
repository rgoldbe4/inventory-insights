import os
from datetime import date
import database

from sqlalchemy.orm.exc import NoResultFound
from werkzeug.utils import secure_filename
from models import *

def newUser(session, email, password, fn, ln):
    session.add(User(email = email, password = password, first_name = fn, last_name = ln))
    session.commit()

def getUser(session, id):
    user = session.query(User).filter_by(id = id).first()
    return user

def editUser(session, id, email, password, fn, ln):
    user = getUser(session, id)
    user.email = email
    user.password = password
    user.first_name = first_name
    user.last_name = last_name

def changePassword(session, id, password):
    user = getUser(session, id)
    user.password = password

def deleteUser(session, id):
    user = getUsers(session, id)
    session.delete(user)