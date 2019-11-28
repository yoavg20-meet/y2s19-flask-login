from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_security

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    fav_food = Column(String)
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password_hash = Column(String)
    fav_food = Column(String)
    def hash_password(self, password):
        self.password_hash = pwd_security.encrypt(password)
    def verify_password(self, password):
        return pwd_security.verify(password, self.password_hash)

Base = declarative_base()

class Product(Base):
   __tablename__ = 'product'
   id = Column(Integer, primary_key=True)
   price = Column(Float)
   name = Column(String)
   picture_link = Column(String)
   description = Column(String)


