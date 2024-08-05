#!/usr/bin/python3
"""
Contains the TestPlaceDocs classes for verifying documentation and style
"""

from datetime import datetime
import inspect
import models
from models import place
from models.base_model import BaseModel
import pep8
import os
import unittest
from sqlalchemy.orm.collections import InstrumentedList
from sqlalchemy.orm.attributes import InstrumentedAttribute
Place = place.Place


class TestPlaceDocs(unittest.TestCase):
    """Tests to ensure documentation and style adherence for the Place class"""
    @classmethod
    def setUpClass(cls):
        """Prepare for documentation tests"""
        cls.place_methods = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_place(self):
        """Verify that models/place.py adheres to PEP8 style guidelines"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style errors (and warnings) found.")

    def test_pep8_conformance_test_place(self):
        """Verify that tests/test_models/test_place.py adheres to PEP8 style guidelines"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style errors (and warnings) found.")

    def test_place_module_docstring(self):
        """Check for the presence of a docstring in the place.py module"""
        self.assertIsNotNone(place.__doc__,
                             "The place.py module requires a docstring")
        self.assertGreaterEqual(len(place.__doc__), 1,
                                "The place.py module requires a docstring")

    def test_place_class_docstring(self):
        """Check for the presence of a docstring in the Place class"""
        self.assertIsNotNone(Place.__doc__,
                             "The Place class requires a docstring")
        self.assertGreaterEqual(len(Place.__doc__), 1,
                                "The Place class requires a docstring")

    def test_place_func_docstrings(self):
        """Ensure that all methods in the Place class have docstrings"""
        for func in self.place_methods:
            self.assertIsNotNone(func[1].__doc__,
                                 f"{func[0]} method lacks a docstring")
            self.assertGreaterEqual(len(func[1].__doc__), 1,
                                    f"{func[0]} method lacks a docstring")


class TestPlace(unittest.TestCase):
    """Tests for the Place class functionality"""
    def test_is_subclass(self):
        """Ensure Place is a subclass of BaseModel"""
        instance = Place()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_city_id_attr(self):
        """Ensure Place has a city_id attribute, and it's an empty string"""
        instance = Place()
        self.assertTrue(hasattr(instance, "city_id"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.city_id)
        else:
            self.assertEqual(instance.city_id, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Testing FileStorage setup")
    def test_city_id_attr_db(self):
        """Ensure Place's city_id attribute is an InstrumentedAttribute in DBStorage"""
        instance = Place()
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertIsInstance(Place.city_id, InstrumentedAttribute)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Testing FileStorage setup")
    def test_user_id_attr_db(self):
        """Ensure Place's user_id attribute is an InstrumentedAttribute in DBStorage"""
        instance = Place()
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertIsInstance(Place.user_id, InstrumentedAttribute)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_user_id_attr(self):
        """Ensure Place has a user_id attribute, and it's an empty string"""
        instance = Place()
        self.assertTrue(hasattr(instance, "user_id"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.user_id)
        else:
            self.assertEqual(instance.user_id, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Testing FileStorage setup")
    def test_name_attr_db(self):
        """Ensure Place's name attribute is an InstrumentedAttribute in DBStorage"""
        instance = Place()
        self.assertTrue(hasattr(Place, "name"))
        self.assertIsInstance(Place.name, InstrumentedAttribute)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_name_attr(self):
        """Ensure Place has a name attribute, and it's an empty string"""
        instance = Place()
        self.assertTrue(hasattr(instance, "name"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.name)
        else:
            self.assertEqual(instance.name, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Testing FileStorage setup")
    def test_description_attr_db(self):
        """Ensure Place's description attribute is an InstrumentedAttribute in DBStorage"""
        instance = Place()
        self.assertTrue(hasattr(Place, "description"))
        self.assertIsInstance(Place.description, InstrumentedAttribute)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_description_attr(self):
        """Ensure Place has a description attribute, and it's an empty string"""
        instance = Place()
        self.assertTrue(hasattr(instance, "description"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.description)
        else:
            self.assertEqual(instance.description, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Testing FileStorage setup")
    def test_number_rooms_attr_db(self):
        """Ensure Place's number_rooms attribute is an InstrumentedAttribute in DBStorage"""
        instance = Place()
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertEqual(instance.number_rooms, None)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_number_rooms_attr(self):
        """Ensure Place has a number_rooms attribute, and it's an integer with value 0"""
        instance = Place()
        self.assertTrue(hasattr(instance, "number_rooms"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.number_rooms)
        else:
            self.assertIsInstance(instance.number_rooms, int)
            self.assertEqual(instance.number_rooms, 0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_number_bathrooms_attr(self):
        """Ensure Place has a number_bathrooms attribute, and it's an integer with value 0"""
        instance = Place()
        self.assertTrue(hasattr(instance, "number_bathrooms"))
        self.assertIsInstance(instance.number_bathrooms, int)
        self.assertEqual(instance.number_bathrooms, 0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Testing FileStorage setup")
    def test_number_rooms_attr_db(self):
        """Ensure Place's number_rooms attribute is an InstrumentedAttribute in DBStorage"""
        instance = Place()
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertEqual(instance.number_rooms, None)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_max_guest_attr(self):
        """Ensure Place has a max_guest attribute, and it's an integer with value 0"""
        instance = Place()
        self.assertTrue(hasattr(instance, "max_guest"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.max_guest)
        else:
            self.assertIsInstance(instance.max_guest, int)
            self.assertEqual(instance.max_guest, 0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_price_by_night_attr(self):
        """Ensure Place has a price_by_night attribute, and it's an integer with value 0"""
        instance = Place()
        self.assertTrue(hasattr(instance, "price_by_night"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.price_by_night)
        else:
            self.assertIsInstance(instance.price_by_night, int)
            self.assertEqual(instance.price_by_night, 0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_latitude_attr(self):
        """Ensure Place has a latitude attribute, and it's a float with value 0.0"""
        instance = Place()
        self.assertTrue(hasattr(instance, "latitude"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.latitude)
        else:
            self.assertIsInstance(instance.latitude, float)
            self.assertEqual(instance.latitude, 0.0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_longitude_attr(self):
        """Ensure Place has a longitude attribute, and it's a float with value 0.0"""
        instance = Place()
        self.assertTrue(hasattr(instance, "longitude"))
        if models.storage_t == 'db':
            self.assertIsNone(instance.longitude)
        else:
            self.assertIsInstance(instance.longitude, float)
            self.assertEqual(instance.longitude, 0.0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage setup")
    def test_amenity_ids_attr(self):
        """Ensure Place has an amenity_ids attribute, and it's an empty list"""
        instance = Place()
        self.assertTrue(hasattr(instance, "amenity_ids"))
        self.assertIsInstance(instance.amenity_ids, list)
        self.assertEqual(len(instance.amenity_ids), 0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Testing FileStorage setup")
    def test_amenities_attr_db(self):
        """Ensure Place's amenities attribute is an InstrumentedList in DBStorage"""
        instance = Place()
        self.assertTrue(hasattr(Place, "amenities"))
        self.assertIsInstance(instance.amenities, InstrumentedList)

    def test_to_dict_creates_dict(self):
        """Ensure the to_dict method creates a dictionary with the correct attributes"""
        instance = Place()
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
        instance = Place()
        dict_representation = instance.to_dict()
        self.assertEqual(dict_representation["__class__"], "Place")
        self.assertIsInstance(dict_representation["created_at"], str)
        self.assertIsInstance(dict_representation["updated_at"], str)
        self.assertEqual(dict_representation["created_at"], instance.created_at.strftime(date_format))
        self.assertEqual(dict_representation["updated_at"], instance.updated_at.strftime(date_format))

    def test_str(self):
        """Verify that the str method outputs the correct string representation"""
        instance = Place()
        expected_str = "[Place] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(expected_str, str(instance))

