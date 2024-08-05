#!/usr/bin/python3
"""
Includes the TestStateDocs class for verifying documentation and style
"""

from datetime import datetime
import inspect
import models
import os
from models import state
from models.base_model import BaseModel
import pep8
import unittest

State = state.State


class TestStateDocs(unittest.TestCase):
    """Checks the documentation and style for the State class"""
    @classmethod
    def setUpClass(cls):
        """Prepare for documentation tests"""
        cls.state_functions = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_compliance_state(self):
        """Verify that models/state.py adheres to PEP8 guidelines"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style errors (or warnings) detected.")

    def test_pep8_compliance_test_state(self):
        """Verify that tests/test_models/test_state.py adheres to PEP8 guidelines"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style errors (or warnings) detected.")

    def test_state_module_docstring(self):
        """Ensure the state.py module has a docstring"""
        self.assertIsNotNone(state.__doc__,
                             "state.py module requires a docstring")
        self.assertGreaterEqual(len(state.__doc__), 1,
                                "state.py module requires a docstring")

    def test_state_class_docstring(self):
        """Ensure the State class has a docstring"""
        self.assertIsNotNone(State.__doc__,
                             "State class requires a docstring")
        self.assertGreaterEqual(len(State.__doc__), 1,
                                "State class requires a docstring")

    def test_state_method_docstrings(self):
        """Verify that all State methods have docstrings"""
        for method in self.state_functions:
            self.assertIsNotNone(method[1].__doc__,
                                 f"{method[0]} method lacks a docstring")
            self.assertGreaterEqual(len(method[1].__doc__), 1,
                                    f"{method[0]} method lacks a docstring")


class TestState(unittest.TestCase):
    """Tests for the State class"""
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Skipping due to DBStorage configuration")
    def test_subclass_of_base_model(self):
        """Verify that State is a subclass of BaseModel"""
        instance = State()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Skipping due to DBStorage configuration")
    def test_name_attribute(self):
        """Verify that State has a name attribute, initially set to an empty string"""
        instance = State()
        self.assertTrue(hasattr(instance, "name"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.name)
        else:
            self.assertEqual(instance.name, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Skipping due to DBStorage configuration")
    def test_to_dict_creates_dictionary(self):
        """Ensure to_dict method creates a dictionary with correct attributes"""
        instance = State()
        dict_representation = instance.to_dict()
        self.assertIsInstance(dict_representation, dict)
        for attr in instance.__dict__:
            if attr != "_sa_instance_state":
                with self.subTest(attr=attr):
                    self.assertIn(attr, dict_representation)
        self.assertIn("__class__", dict_representation)
        del instance

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Skipping due to DBStorage configuration")
    def test_to_dict_values(self):
        """Check that values in the dictionary returned by to_dict are correct"""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        instance = State()
        dict_representation = instance.to_dict()
        self.assertEqual(dict_representation["__class__"], "State")
        self.assertIsInstance(dict_representation["created_at"], str)
        self.assertIsInstance(dict_representation["updated_at"], str)
        self.assertEqual(dict_representation["created_at"], instance.created_at.strftime(date_format))
        self.assertEqual(dict_representation["updated_at"], instance.updated_at.strftime(date_format))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Skipping due to DBStorage configuration")
    def test_str_method_output(self):
        """Verify that the str method provides the correct string representation"""
        instance = State()
        expected_str = "[State] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(expected_str, str(instance))

