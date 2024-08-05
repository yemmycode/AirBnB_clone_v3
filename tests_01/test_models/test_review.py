#!/usr/bin/python3
"""
Includes the TestReviewDocs class for verifying documentation and style
"""

from datetime import datetime
import inspect
import models
from models import review
from models.base_model import BaseModel
import pep8
import os
import unittest

Review = review.Review


class TestReviewDocs(unittest.TestCase):
    """Checks documentation and style for the Review class"""
    @classmethod
    def setUpClass(cls):
        """Prepare for documentation tests"""
        cls.review_methods = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Verify that models/review.py adheres to PEP8 guidelines"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style errors (or warnings) detected.")

    def test_pep8_conformance_test_review(self):
        """Verify that tests/test_models/test_review.py adheres to PEP8 guidelines"""
        pep8_checker = pep8.StyleGuide(quiet=True)
        result = pep8_checker.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style errors (or warnings) detected.")

    def test_review_module_docstring(self):
        """Check for a docstring in the review.py module"""
        self.assertIsNotNone(review.__doc__,
                             "review.py module requires a docstring")
        self.assertGreaterEqual(len(review.__doc__), 1,
                                "review.py module requires a docstring")

    def test_review_class_docstring(self):
        """Check for a docstring in the Review class"""
        self.assertIsNotNone(Review.__doc__,
                             "Review class requires a docstring")
        self.assertGreaterEqual(len(Review.__doc__), 1,
                                "Review class requires a docstring")

    def test_review_method_docstrings(self):
        """Ensure all Review methods have docstrings"""
        for method in self.review_methods:
            self.assertIsNotNone(method[1].__doc__,
                                 f"{method[0]} method lacks a docstring")
            self.assertGreaterEqual(len(method[1].__doc__), 1,
                                    f"{method[0]} method lacks a docstring")


class TestReview(unittest.TestCase):
    """Tests for the Review class"""
    def test_is_subclass(self):
        """Verify that Review is a subclass of BaseModel"""
        instance = Review()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_place_id_attribute(self):
        """Verify Review has a place_id attribute, and it's an empty string"""
        instance = Review()
        self.assertTrue(hasattr(instance, "place_id"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.place_id)
        else:
            self.assertEqual(instance.place_id, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_user_id_attribute(self):
        """Verify Review has a user_id attribute, and it's an empty string"""
        instance = Review()
        self.assertTrue(hasattr(instance, "user_id"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.user_id)
        else:
            self.assertEqual(instance.user_id, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_text_attribute(self):
        """Verify Review has a text attribute, and it's an empty string"""
        instance = Review()
        self.assertTrue(hasattr(instance, "text"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.text)
        else:
            self.assertEqual(instance.text, "")

    def test_to_dict_creates_dict(self):
        """Ensure to_dict method creates a dictionary with the correct attributes"""
        instance = Review()
        dict_representation = instance.to_dict()
        self.assertIsInstance(dict_representation, dict)
        for attr in instance.__dict__:
            if attr != "_sa_instance_state":
                with self.subTest(attr=attr):
                    self.assertIn(attr, dict_representation)
        self.assertIn("__class__", dict_representation)

    def test_to_dict_values(self):
        """Check that values in the dictionary returned by to_dict are correct"""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        instance = Review()
        dict_representation = instance.to_dict()
        self.assertEqual(dict_representation["__class__"], "Review")
        self.assertIsInstance(dict_representation["created_at"], str)
        self.assertIsInstance(dict_representation["updated_at"], str)
        self.assertEqual(dict_representation["created_at"], instance.created_at.strftime(date_format))
        self.assertEqual(dict_representation["updated_at"], instance.updated_at.strftime(date_format))

    def test_str_method(self):
        """Verify that the str method outputs the correct string representation"""
        instance = Review()
        expected_str = "[Review] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(expected_str, str(instance))
