from sqlalchemy_serializer import SerializerMixin

import database
from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, Boolean, Float, Date, Table
from sqlalchemy.orm import relationship


association_cart_table = Table('cart_item', database.Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('cart_id', Integer, ForeignKey('cart.id')),
    Column('item_id', Integer, ForeignKey('item.id')),
    Column('quantity', Integer, default=1)
)

association_order_table = Table('order_item', database.Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('order_id', Integer, ForeignKey('order.id')),
    Column('item_id', Integer, ForeignKey('item.id')),
    Column('quantity', Integer, default=1)
)

# Licensing per Admin
class License(database.Base, SerializerMixin):
  __tablename__ = 'license'

  id = Column(Integer, primary_key=True)
  accounts = Column(Integer)
  name = Column(String)

  def default(self, o):
    return o.__dict__


# Customer who bought our product
class Administrator(database.Base, SerializerMixin):
  __tablename__ = 'administrator'

  id = Column(Integer, primary_key=True)
  email = Column(String(100))
  first_name = Column(String(50))
  last_name = Column(String(50))
  owner = Column(Boolean)
  password = Column(String(100))

  license_id = Column(Integer, ForeignKey('license.id'))
  license = relationship('License', uselist=False)

  def default(self, o):
    return o.__dict__


# Person who uses an Administrator website
class User(database.Base, SerializerMixin):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True)
  email = Column(String(100))
  password = Column(String(100))
  first_name = Column(String(50))
  last_name = Column(String(50))

  # Relationships
  carts = relationship('Cart')
  orders = relationship('Order')

  def default(self, o):
    return o.__dict__


# Item that the Administrator provides
class Item(database.Base, SerializerMixin):
  __tablename__ = 'item'

  id = Column(Integer, primary_key=True)
  name = Column(String(50))
  price = Column(Float)
  discontinued = Column(Boolean)
  description = Column(String(500))
  cost = Column(Float)
  category = Column(String(50))
  image = Column(String(100))
  instock = Column(Integer)

  # Relationships
  recommendation_id = Column(Integer, ForeignKey('recommendation.id'))
  license_id = Column(Integer, ForeignKey('license.id'))
  license = relationship('License', uselist=False)

  def default(self, o):
    return o.__dict__

  # A list of items desired by the User.
# This may change. Look at "Order" if you want a finalized Cart.
class Cart(database.Base, SerializerMixin):
  __tablename__ = 'cart'

  id = Column(Integer, primary_key=True)

  items = relationship('Item', secondary=association_cart_table)
  user_id = Column(Integer, ForeignKey('user.id'))
  active = Column(Boolean)
  recommendation_id = Column(Integer, ForeignKey('recommendation.id'))

  def default(self, o):
    return o.__dict__


# A list of items purchased by the User.
class Order(database.Base, SerializerMixin):
  __tablename__ = 'order'

  id = Column(Integer, primary_key=True)

  user_id = Column(Integer, ForeignKey('user.id'))
  items = relationship('Item', secondary=association_order_table)
  date = Column(Date)

  def default(self, o):
    return o.__dict__


# Shows what item, cart, and success of a Recommended item.
class Recommendation(database.Base, SerializerMixin):
  __tablename__ = 'recommendation'

  id = Column(Integer, primary_key=True)
  cart = relationship('Cart', uselist=False)

  recommended = relationship('Item', uselist=False)
  success = Column(Boolean)

  def default(self, o):
    return o.__dict__


