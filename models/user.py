#!/usr/bin/python3
"""Defines the User class"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib

class User(BaseModel, Base):
    """User class representing a user entity"""
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
        """Initializes a new user instance"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, key, value):
        """Hashes the password before setting it"""
        if key == "password":
            value = hashlib.md5(value.encode()).hexdigest()
        super().__setattr__(key, value)
