#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the User class"""
=======
""" holds class User"""
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
<<<<<<< HEAD
import hashlib

class User(BaseModel, Base):
    """User class representing a user entity"""
=======


class User(BaseModel, Base):
    """Representation of a user """
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
        """Initializes a new user instance"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, key, value):
        """Hashes the password before setting it"""
        if key == "password":
            value = hashlib.md5(value.encode()).hexdigest()
        super().__setattr__(key, value)
=======
        """initializes user"""
        super().__init__(*args, **kwargs)
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
