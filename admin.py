import os
from datetime import date
import database

from sqlalchemy.orm.exc import NoResultFound
from werkzeug.utils import secure_filename
from models import *

def newAdmin(session, email, fn, ln, own, pw):
    session.add(Administrator(email = email, first_name = fn, last_name = ln, owner = own, password = password))
    session.commit()

def getAdmin(session, id):
    admin = session.query(Administrator).filter_by(id = id).first()
    return admin

def editAdmin(session, id, email, fn, ln, own, pw):
    admin = getAdmin(session, id)
    admin.email = email
    admin.first_name = fn
    admin.last_name = ln
    admin.owner = own
    admin.password = pw

def changeAdminPassword(session, id, pw):
    admin = getAdmin(session, id)
    admin.password = pw

def deleteAdmin(session, id):
    admin = getAdmin(session, id)
    session.delete(admin)
