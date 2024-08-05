#!/usr/bin/env python3
"""
Module containing tests for the FileStorage class documentation and functionality.
"""

from datetime import datetime
import inspect
import models
from models.engine import file_storage
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

FileStorage = file_storage.FileStorage
classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

class TestFileStorageDocs(unittest.TestCase):
    """Checks documentation and style for the FileStorage class."""
    
    @classmethod
    def setUpClass(cls):
        """Prepares for documentation tests."""
        cls.fs_functions = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """Verifies PEP 8 compliance for file_storage.py."""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (or warnings) found.")

    def test_pep8_conformance_test_file_storage(self):
        """Verifies PEP 8 compliance for test_file_storage.py."""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors (or warnings) found.")

    def test_file_storage_module_docstring(self):
        """Checks if file_storage.py has a module docstring."""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py module is missing a docstring.")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py module docstring is too short.")

    def test_file_storage_class_docstring(self):
        """Checks if FileStorage class has a docstring."""
        self.assertIsNot(FileStorage.__doc__, None,
                         "FileStorage class is missing a docstring.")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "FileStorage class docstring is too short.")

    def test_fs_func_docstrings(self):
        """Checks if all FileStorage methods have docstrings."""
        for function in self.fs_functions:
            self.assertIsNot(function[1].__doc__, None,
                             "{:s} method is missing a docstring".format(function[0]))
            self.assertTrue(len(function[1].__doc__) >= 1,
                            "{:s} method has a short docstring".format(function[0]))

class TestFileStorage(unittest.TestCase):
    """Tests the functionality of the FileStorage class."""

    @unittest.skipIf(models.storage_t == 'db', "Skipping tests for file storage.")
    def test_all_returns_dict(self):
        """Ensures that all() returns the FileStorage.__objects attribute."""
        storage = FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIs(all_objects, storage._FileStorage__objects)

    @unittest.skipIf(models.storage_t == 'db', "Skipping tests for file storage.")
    def test_new(self):
        """Tests that new() correctly adds an object to the FileStorage.__objects attribute."""
        storage = FileStorage()
        original_objects = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_objects = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = f"{instance.__class__.__name__}.{instance.id}"
                storage.new(instance)
                test_objects[instance_key] = instance
                self.assertEqual(test_objects, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = original_objects

    @unittest.skipIf(models.storage_t == 'db', "Skipping tests for file storage.")
    def test_save(self):
        """Tests that save() properly writes objects to file.json."""
        storage = FileStorage()
        test_objects = {}
        for key, value in classes.items():
            instance = value()
            instance_key = f"{instance.__class__.__name__}.{instance.id}"
            test_objects[instance_key] = instance
        original_objects = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = test_objects
        storage.save()
        FileStorage._FileStorage__objects = original_objects
        for key, value in test_objects.items():
            test_objects[key] = value.to_dict()
        test_json = json.dumps(test_objects)
        with open("file.json", "r") as file:
            file_contents = file.read()
        self.assertEqual(json.loads(test_json), json.loads(file_contents))

    def test_get_dbstorage(self):
        """Tests the get() method with valid data."""
        state = State(name="Some state")
        state.save()
        models.storage.save()
        state_id = list(models.storage.all(State).values())[0].id
        retrieved_state = str(models.storage.all()['State.' + state_id])
        self.assertIsNotNone(retrieved_state)

    def test_get_dbstorage2(self):
        """Tests get() with valid data and verifies count() method."""
        count_all = models.storage.count()
        self.assertIsInstance(count_all, int)
        count_state = models.storage.count(State)
        self.assertIsInstance(count_state, int)
        state_id = list(models.storage.all(State).values())[0].id
        retrieved_state = models.storage.get(State, state_id)
        self.assertEqual(str(type(retrieved_state)), "<class 'models.state.State'>")

    def test_get_fstorage_none(self):
        """Tests the get() method with invalid input."""
        state = State(name="Some state")
        state.save()
        invalid_retrieval = models.storage.get('State', 'invalid_id')
        self.assertIsNone(invalid_retrieval)
        invalid_class_retrieval = models.storage.get('NonExistentClass', state.id)
        self.assertIsNone(invalid_class_retrieval)
        invalid_id_retrieval = models.storage.get('State', 33333)
        self.assertIsNone(invalid_id_retrieval)

    def test_count_fstorage(self):
        """Tests the count() method."""
        initial_count = models.storage.count()
        state = State(name="Some state")
        state.save()
        new_count = models.storage.count()
        self.assertEqual(initial_count + 1, new_count)

    def test_count_fstorage_cls(self):
        """Tests the count() method with a class name."""
        initial_count = models.storage.count()
        initial_state_count = models.storage.count('State')
        state = State(name="New York")
        state.save()
        new_count = models.storage.count()
        new_state_count = models.storage.count('State')
        self.assertEqual(initial_count + 1, new_count)
        self.assertEqual(initial_state_count + 1, new_state_count)
