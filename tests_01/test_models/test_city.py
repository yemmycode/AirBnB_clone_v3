#!/usr/bin/python3
"""
Contains the TestCityDocs classes for documentation and style checks
"""

from datetime import datetime
import inspect
from models import city
from models.base_model import BaseModel
import os
import pep8
import unittest
from sqlalchemy.orm.attributes import InstrumentedAttribute
City = city.City


class TestCityDocs(unittest.TestCase):
    """Tests to verify the documentation and style of the City class"""
    @classmethod
    def setUpClass(cls):
        """Setup for the docstring tests"""
        cls.city_methods = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test that models/city.py follows PEP8 style guidelines"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found PEP8 style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test that tests/test_models/test_city.py follows PEP8 style guidelines"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found PEP8 style errors (and warnings).")

    def test_city_module_docstring(self):
        """Test for the presence of a docstring in the city.py module"""
        self.assertIsNotNone(city.__doc__,
                             "city.py needs a docstring")
        self.assertGreaterEqual(len(city.__doc__), 1,
                                "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for the presence of a docstring in the City class"""
        self.assertIsNotNone(City.__doc__,
                             "City class needs a docstring")
        self.assertGreaterEqual(len(City.__doc__), 1,
                                "City class needs a docstring")

    def test_city_func_docstrings(self):
        """Test for the presence of docstrings in City methods"""
        for func in self.city_methods:
            self.assertIsNotNone(func[1].__doc__,
                                 f"{func[0]} method needs a docstring")
            self.assertGreaterEqual(len(func[1].__doc__), 1,
                                    f"{func[0]} method needs a docstring")


class TestCity(unittest.TestCase):
    """Tests for the City class functionality"""
    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        city_instance = City()
        self.assertIsInstance(city_instance, BaseModel)
        self.assertTrue(hasattr(city_instance, "id"))
        self.assertTrue(hasattr(city_instance, "created_at"))
        self.assertTrue(hasattr(city_instance, "updated_at"))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage")
    def test_name_attr(self):
        """Test that City has an attribute name that is an empty string"""
        city_instance = City()
        self.assertTrue(hasattr(city_instance, "name"))
        self.assertEqual(city_instance.name, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Testing FileStorage")
    def test_name_attr_db(self):
        """Test for the name attribute in DBStorage"""
        city_instance = City()
        self.assertTrue(hasattr(City, "name"))
        self.assertIsInstance(City.name, InstrumentedAttribute)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage")
    def test_state_id_attr(self):
        """Test that City has an attribute state_id that is an empty string"""
        city_instance = City()
        self.assertTrue(hasattr(city_instance, "state_id"))
        self.assertEqual(city_instance.state_id, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Testing FileStorage")
    def test_state_id_attr_db(self):
        """Test for the state_id attribute in DBStorage"""
        city_instance = City()
        self.assertTrue(hasattr(City, "state_id"))
        self.assertIsInstance(City.state_id, InstrumentedAttribute)

    def test_to_dict_creates_dict(self):
        """Test that to_dict method creates a dictionary with correct attributes"""
        city_instance = City()
        city_dict = city_instance.to_dict()
        self.assertIsInstance(city_dict, dict)
        for attr in city_instance.__dict__:
            if attr != "_sa_instance_state":
                with self.subTest(attr=attr):
                    self.assertIn(attr, city_dict)
        self.assertIn("__class__", city_dict)

    def test_to_dict_values(self):
        """Test that the values in the dictionary returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        city_instance = City()
        city_dict = city_instance.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)
        self.assertEqual(city_dict["created_at"], city_instance.created_at.strftime(time_format))
        self.assertEqual(city_dict["updated_at"], city_instance.updated_at.strftime(time_format))

    def test_str(self):
        """Test that the __str__ method has the correct output"""
        city_instance = City()
        expected_str = "[City] ({}) {}".format(city_instance.id, city_instance.__dict__)
        self.assertEqual(expected_str, str(city_instance))
