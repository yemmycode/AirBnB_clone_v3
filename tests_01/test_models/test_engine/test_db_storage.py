#!/usr/bin/python3
"""
Includes the TestDBStorageDocs and TestDBStorage classes for DBStorage documentation and functionality testing
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest

DBStorage = db_storage.DBStorage
class_mapping = {"Amenity": Amenity, "City": City, "Place": Place,
                  "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Verifies documentation and style compliance for DBStorage class"""
    
    @classmethod
    def setUpClass(cls):
        """Prepare for documentation and style tests"""
        cls.db_storage_functions = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Check PEP8 compliance for models/engine/db_storage.py"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style issues found.")

    def test_pep8_conformance_test_db_storage(self):
        """Check PEP8 compliance for tests/test_models/test_db_storage.py"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['tests/test_models/test_engine/test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style issues found.")

    def test_db_storage_module_docstring(self):
        """Ensure the db_storage.py module has a docstring"""
        self.assertIsNotNone(db_storage.__doc__,
                             "db_storage.py module requires a docstring")
        self.assertGreaterEqual(len(db_storage.__doc__), 1,
                                "db_storage.py module docstring is too short")

    def test_db_storage_class_docstring(self):
        """Ensure the DBStorage class has a docstring"""
        self.assertIsNotNone(DBStorage.__doc__,
                             "DBStorage class requires a docstring")
        self.assertGreaterEqual(len(DBStorage.__doc__), 1,
                                "DBStorage class docstring is too short")

    def test_db_storage_method_docstrings(self):
        """Ensure all methods in DBStorage have docstrings"""
        for function in self.db_storage_functions:
            self.assertIsNotNone(function[1].__doc__,
                                 f"{function[0]} method is missing a docstring")
            self.assertGreaterEqual(len(function[1].__doc__), 1,
                                    f"{function[0]} method docstring is too short")

    def test_get_method_valid_data(self):
        """Verify the get method with valid data"""
        obj = State(name="Some state")
        obj.save()
        models.storage.save()
        retrieved_obj_id = list(models.storage.all(State).values())[0].id
        retrieved_obj_str = str(models.storage.all()['State.' + retrieved_obj_id])
        self.assertIsNotNone(retrieved_obj_str)

    def test_get_method_valid_data_count(self):
        """Verify count method functionality"""
        total_count = models.storage.count()
        self.assertIsInstance(total_count, int)
        class_count = models.storage.count(State)
        self.assertIsInstance(class_count, int)
        first_state_id = list(models.storage.all(State).values())[0].id
        retrieved_instance = models.storage.get(State, first_state_id)
        self.assertEqual(str(type(retrieved_instance)), "<class 'models.state.State'>")

    def test_get_method_invalid_input(self):
        """Test the get method with invalid input"""
        obj = State(name="Some state")
        obj.save()
        invalid_result1 = models.storage.get('State', 'invalid_id')
        self.assertIsNone(invalid_result1)
        invalid_result2 = models.storage.get('InvalidClass', obj.id)
        self.assertIsNone(invalid_result2)
        invalid_result3 = models.storage.get('State', 99999)
        self.assertIsNone(invalid_result3)

    def test_count_method(self):
        """Verify the count method functionality"""
        initial_count = models.storage.count()
        obj = State(name="Some state")
        obj.save()
        updated_count = models.storage.count()
        self.assertEqual(initial_count + 1, updated_count)

    def test_count_method_with_class(self):
        """Verify the count method with class name"""
        initial_count = models.storage.count()
        initial_class_count = models.storage.count('State')
        obj = State(name="New York")
        obj.save()
        updated_count = models.storage.count()
        updated_class_count = models.storage.count('State')
        self.assertEqual(initial_count + 1, updated_count)
        self.assertEqual(initial_class_count + 1, updated_class_count)
