#!/usr/bin/python3
"""
Includes the TestUserDocs class for verifying documentation and code style
"""

from datetime import datetime
import inspect
import models
from models import user
from models.base_model import BaseModel
import pep8
import os
import unittest

User = user.User


class TestUserDocs(unittest.TestCase):
    """Checks documentation and style for the User class"""
    @classmethod
    def setUpClass(cls):
        """Prepare for documentation and style tests"""
        cls.user_functions = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_compliance_user(self):
        """Verify that models/user.py adheres to PEP8 standards"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style errors or warnings detected.")

    def test_pep8_compliance_test_user(self):
        """Verify that tests/test_models/test_user.py adheres to PEP8 standards"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style errors or warnings detected.")

    def test_user_module_docstring(self):
        """Check for a docstring in the user.py module"""
        self.assertIsNotNone(user.__doc__,
                             "user.py module requires a docstring")
        self.assertGreaterEqual(len(user.__doc__), 1,
                                "user.py module requires a docstring")

    def test_user_class_docstring(self):
        """Check for a docstring in the User class"""
        self.assertIsNotNone(User.__doc__,
                             "User class requires a docstring")
        self.assertGreaterEqual(len(User.__doc__), 1,
                                "User class requires a docstring")

    def test_user_method_docstrings(self):
        """Ensure all User methods have docstrings"""
        for function in self.user_functions:
            self.assertIsNotNone(function[1].__doc__,
                                 f"{function[0]} method lacks a docstring")
            self.assertGreaterEqual(len(function[1].__doc__), 1,
                                    f"{function[0]} method lacks a docstring")


class TestUser(unittest.TestCase):
    """Tests for the User class"""
    def test_subclass_of_base_model(self):
        """Verify that User is a subclass of BaseModel"""
        instance = User()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Skipping due to DBStorage configuration")
    def test_email_attribute(self):
        """Verify that User has an email attribute, initially an empty string"""
        instance = User()
        self.assertTrue(hasattr(instance, "email"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.email)
        else:
            self.assertEqual(instance.email, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Skipping due to DBStorage configuration")
    def test_password_attribute(self):
        """Verify that User has a password attribute, initially an empty string"""
        instance = User()
        self.assertTrue(hasattr(instance, "password"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.password)
        else:
            self.assertEqual(instance.password, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Skipping due to DBStorage configuration")
    def test_first_name_attribute(self):
        """Verify that User has a first_name attribute, initially an empty string"""
        instance = User()
        self.assertTrue(hasattr(instance, "first_name"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.first_name)
        else:
            self.assertEqual(instance.first_name, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Skipping due to DBStorage configuration")
    def test_last_name_attribute(self):
        """Verify that User has a last_name attribute, initially an empty string"""
        instance = User()
        self.assertTrue(hasattr(instance, "last_name"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.last_name)
        else:
            self.assertEqual(instance.last_name, "")

    def test_to_dict_creates_dictionary(self):
        """Ensure to_dict method generates a dictionary with correct attributes"""
        instance = User()
        dict_representation = instance.to_dict()
        self.assertIsInstance(dict_representation, dict)
        for attr in instance.__dict__:
            if attr != "_sa_instance_state":
                with self.subTest(attr=attr):
                    self.assertIn(attr, dict_representation)
        self.assertIn("__class__", dict_representation)

    def test_to_dict_values(self):
        """Verify that values in the dictionary returned by to_dict are accurate"""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        instance = User()
        dict_representation = instance.to_dict()
        self.assertEqual(dict_representation["__class__"], "User")
        self.assertIsInstance(dict_representation["created_at"], str)
        self.assertIsInstance(dict_representation["updated_at"], str)
        self.assertEqual(dict_representation["created_at"], instance.created_at.strftime(date_format))
        self.assertEqual(dict_representation["updated_at"], instance.updated_at.strftime(date_format))

    def test_str_method_output(self):
        """Verify that the str method produces the correct string representation"""
        instance = User()
        expected_str = "[User] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(expected_str, str(instance))
