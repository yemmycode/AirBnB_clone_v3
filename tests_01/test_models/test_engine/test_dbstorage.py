#!/usr/bin/env python3
"""
Module containing the TestDBStorageDocs and TestDBStorage classes.
"""

from datetime import datetime
import inspect
import models
from models.engine import file_storage
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import MySQLdb
import json
import os
import pep8
import unittest

FileStorage = file_storage.FileStorage
DBStorage = db_storage.DBStorage
classes = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

class TestDBStorageDocs(unittest.TestCase):
    """Tests for documentation and style."""
    
    @classmethod
    def setUpClass(cls):
        """Sets up for documentation tests."""
        cls.dbs_functions = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Checks PEP 8 compliance for db_storage.py."""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (and warnings) found.")

    def test_pep8_conformance_test_db_storage(self):
        """Checks PEP 8 compliance for test_dbstorage.py."""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['tests/test_models/test_engine/test_dbstorage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (and warnings) found.")

    def test_db_storage_module_docstring(self):
        """Tests if db_storage.py has a module docstring."""
        self.assertIsNot(db_storage.__doc__, None,
                         "Module docstring missing in db_storage.py")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "Module docstring in db_storage.py is too short")

    def test_db_storage_class_docstring(self):
        """Tests if DBStorage class has a docstring."""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class docstring missing")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class docstring is too short")

    def test_dbs_functions_docstrings(self):
        """Tests docstrings for all DBStorage methods."""
        for func in self.dbs_functions:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method is missing a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method has a short docstring".format(func[0]))

@unittest.skipIf(models.is_db != 'db', 'Skipping DBStorage tests')
class TestDBStorage(unittest.TestCase):
    """Tests for DBStorage methods."""

    @classmethod
    def setUpClass(cls):
        """Sets up the test environment."""
        cls.user = User()
        cls.user.first_name = "123"
        cls.user.last_name = "321"
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Cleans up after tests."""
        del cls.user

    def remove_file(self):
        """Removes the file.json if it exists."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_all(self):
        """Tests the all method of FileStorage."""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new_method(self):
        """Tests the new method of FileStorage."""
        storage = FileStorage()
        user = User()
        user.id = str(123455)
        user.name = "Kevin"
        storage.new(user)
        key = f"{user.__class__.__name__}.{user.id}"
        self.assertIsNotNone(storage.all().get(key))

    def test_reload_storage(self):
        """Tests the reload method of FileStorage."""
        self.storage.save()
        root_path = os.path.dirname(os.path.abspath("console.py"))
        file_path = os.path.join(root_path, "file.json")
        with open(file_path, 'r') as file:
            initial_lines = file.readlines()
        try:
            os.remove(file_path)
        except Exception:
            pass
        self.storage.save()
        with open(file_path, 'r') as file:
            updated_lines = file.readlines()
        self.assertEqual(initial_lines, updated_lines)
        try:
            os.remove(file_path)
        except Exception:
            pass
        with open(file_path, "w") as file:
            file.write("{}")
        with open(file_path, "r") as file:
            for line in file:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)
