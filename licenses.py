import os
from datetime import date
import database

from sqlalchemy.orm.exc import NoResultFound
from werkzeug.utils import secure_filename
from models import *

def newLicense(session, numusers):
    session.add(License(accounts = numusers))
    session.commit()

def getLicense(session, license_id):
    ourLicense = session.query(License).filter_by(id=license_id).first()
    return ourLicense

def editLicense(session, license_id, numUsers):
    ourLicense = getLicense(session, license_id)
    ourLicense.numUsers = license_id

def deleteLicense(session, license_id):
    ourLicense = getLicense(session, license_id)
    session.delete(ourLicense)
