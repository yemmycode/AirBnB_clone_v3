#!/usr/bin/python3
"""
Defines the test cases for the Amenity class and its documentation
"""

from datetime import datetime
import inspect
from models import amenity
from models.base_model import BaseModel
import os
import pep8
import unittest
from sqlalchemy.orm.attributes import InstrumentedAttribute
Amenity = amenity.Amenity


class TestAmenityDocs(unittest.TestCase):
    """Tests for the documentation and style compliance of the Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Setup for docstring tests"""
        cls.amenity_functions = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Test that models/amenity.py follows PEP8 guidelines"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """Test that tests/test_models/test_amenity.py follows PEP8 guidelines"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """Test for the presence of a module docstring in amenity.py"""
        self.assertIsNotNone(amenity.__doc__, "amenity.py needs a docstring")
        self.assertGreaterEqual(len(amenity.__doc__), 1, "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """Test for the presence of a docstring in the Amenity class"""
        self.assertIsNotNone(Amenity.__doc__, "Amenity class needs a docstring")
        self.assertGreaterEqual(len(Amenity.__doc__), 1, "Amenity class needs a docstring")

    def test_amenity_func_docstrings(self):
        """Test that all functions in Amenity have docstrings"""
        for func in self.amenity_functions:
            self.assertIsNotNone(func[1].__doc__, f"{func[0]} method needs a docstring")
            self.assertGreaterEqual(len(func[1].__doc__), 1, f"{func[0]} method needs a docstring")


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity_instance = Amenity()
        self.assertIsInstance(amenity_instance, BaseModel)
        self.assertTrue(hasattr(amenity_instance, "id"))
        self.assertTrue(hasattr(amenity_instance, "created_at"))
        self.assertTrue(hasattr(amenity_instance, "updated_at"))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Testing DBStorage")
    def test_name_attr(self):
        """Test that Amenity has attribute 'name' with an empty string"""
        amenity_instance = Amenity()
        self.assertTrue(hasattr(amenity_instance, "name"))
        self.assertEqual(amenity_instance.name, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Testing FileStorage")
    def test_name_attr_db(self):
        """Test for DBStorage 'name' attribute"""
        amenity_instance = Amenity()
        self.assertTrue(hasattr(Amenity, "name"))
        self.assertIsInstance(Amenity.name, InstrumentedAttribute)

    def test_to_dict_creates_dict(self):
        """Test that to_dict method creates a dictionary with correct attributes"""
        amenity_instance = Amenity()
        new_dict = amenity_instance.to_dict()
        self.assertIsInstance(new_dict, dict)
        for attr in amenity_instance.__dict__:
            if attr != "_sa_instance_state":
                with self.subTest(attr=attr):
                    self.assertIn(attr, new_dict)
        self.assertIn("__class__", new_dict)

    def test_to_dict_values(self):
        """Test that the dictionary values from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        amenity_instance = Amenity()
        new_dict = amenity_instance.to_dict()
        self.assertEqual(new_dict["__class__"], "Amenity")
        self.assertIsInstance(new_dict["created_at"], str)
        self.assertIsInstance(new_dict["updated_at"], str)
        self.assertEqual(new_dict["created_at"], amenity_instance.created_at.strftime(time_format))
        self.assertEqual(new_dict["updated_at"], amenity_instance.updated_at.strftime(time_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        amenity_instance = Amenity()
        expected_str = "[Amenity] ({}) {}".format(amenity_instance.id, amenity_instance.__dict__)
        self.assertEqual(expected_str, str(amenity_instance))


if __name__ == "__main__":
    unittest.main()
