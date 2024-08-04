#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
import models
<<<<<<< HEAD
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from os import getenv

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base() if models.storage_t == "db" else object

class BaseModel:
    """The BaseModel class from which future classes will be derived"""

=======
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
<<<<<<< HEAD
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)
        if isinstance(self.created_at, str):
            self.created_at = datetime.strptime(self.created_at, TIME_FORMAT)
        if isinstance(self.updated_at, str):
            self.updated_at = datetime.strptime(self.updated_at, TIME_FORMAT)

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
=======
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

<<<<<<< HEAD
    def to_dict(self, secure_pwd=True):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(TIME_FORMAT)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(TIME_FORMAT)
        new_dict["__class__"] = self.__class__.__name__
        new_dict.pop("_sa_instance_state", None)
        if secure_pwd and 'password' in new_dict:
            del new_dict['password']
        return new_dict

    def delete(self):
        """Deletes the current instance from the storage"""
=======
    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
        models.storage.delete(self)
