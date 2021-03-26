import database
from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship


class License(database.Base):
  __tablename__ = 'license'

  id = Column(Integer, primary_key=True)
  accounts = Column(Integer)
