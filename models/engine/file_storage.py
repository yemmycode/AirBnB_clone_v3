#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "Amenity": Amenity, 
    "BaseModel": BaseModel, 
    "City": City,
    "Place": Place, 
    "Review": Review, 
    "State": State, 
    "User": User
}

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls:
            return {key: value for key, value in self.__objects.items() if isinstance(value, cls) or cls == value.__class__.__name__}
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict(False) for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls_name = value["__class__"]
                self.__objects[key] = classes[cls_name](**value)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it’s inside"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects.pop(key, None)

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """Retrieves an object"""
        if cls in classes.values() and isinstance(id, str):
            return self.__objects.get(f"{cls.__name__}.{id}")
        return None

    def count(self, cls=None):
        """Counts the number of objects"""
        return len(self.all(cls))
