#!/usr/bin/python3
"""
Contains the TestStateDocs classes
"""

from datetime import datetime
import inspect
import models
import os
from models import state
from models.base_model import BaseModel
import pep8
import unittest
from api.v1 import app
from api.v1.views import states as test_state
from api.v1.views import amenities
from api.v1.views import cities
from api.v1.views import index
from api.v1.views import places_reviews
from api.v1.views import places_amenities
from api.v1.views import places
from api.v1.views import users
State = state.State


class TestStateDocs(unittest.TestCase):
    """Tests for the documentation of all api files"""
    
    @classmethod
    def setUpClass(cls):
        """Initialize setup for doc tests"""
        cls.state_f = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_app(self):
        """Check PEP8 compliance for api/v1/app.py."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/app.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_states(self):
        """Check PEP8 compliance for api/v1/views/states.py."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/states.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_amenities(self):
        """Check PEP8 compliance for api/v1/views/amenities.py."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/amenities.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_cities(self):
        """Check PEP8 compliance for api/v1/views/cities.py."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/cities.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_places_reviews(self):
        """Check PEP8 compliance for api/v1/views/places_reviews.py."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/places_reviews.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_places(self):
        """Check PEP8 compliance for api/v1/views/places.py."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/places.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_users(self):
        """Check PEP8 compliance for api/v1/views/users.py."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/users.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_index(self):
        """Check PEP8 compliance for api/v1/views/index.py."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/index.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_pep8(self):
        """Check PEP8 compliance for tests/test_api/test_pep8.py."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_api/test_pep8.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_places_amenities(self):
        """Check PEP8 compliance for api/v1/views/places_amenities.py."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['api/v1/views/places_amenities.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_state_module_docstring_app(self):
        """Check for the module docstring in api/v1/app.py"""
        self.assertIsNot(app.__doc__, None,
                         "app.py needs a docstring")
        self.assertTrue(len(app.__doc__) >= 1,
                        "app.py needs a docstring")

    def test_state_class_docstring_state(self):
        """Check for the class docstring in api/v1/views/states.py"""
        self.assertIsNot(test_state.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(test_state.__doc__) >= 1,
                        "State class needs a docstring")

    def test_state_class_docstring_amenities(self):
        """Check for the class docstring in api/v1/views/amenities.py"""
        self.assertIsNot(amenities.__doc__, None,
                         "Amenities class needs a docstring")
        self.assertTrue(len(amenities.__doc__) >= 1,
                        "Amenities class needs a docstring")

    def test_state_class_docstring_cities(self):
        """Check for the class docstring in api/v1/views/cities.py"""
        self.assertIsNot(cities.__doc__, None,
                         "Cities class needs a docstring")
        self.assertTrue(len(cities.__doc__) >= 1,
                        "Cities class needs a docstring")

    def test_state_class_docstring_index(self):
        """Check for the class docstring in api/v1/views/index.py"""
        self.assertIsNot(index.__doc__, None,
                         "Index class needs a docstring")
        self.assertTrue(len(index.__doc__) >= 1,
                        "Index class needs a docstring")

    def test_state_class_docstring_reviews(self):
        """Check for the class docstring in api/v1/views/places_reviews.py"""
        self.assertIsNot(places_reviews.__doc__, None,
                         "PlacesReviews class needs a docstring")
        self.assertTrue(len(places_reviews.__doc__) >= 1,
                        "PlacesReviews class needs a docstring")

    def test_state_class_docstring_places(self):
        """Check for the class docstring in api/v1/views/places.py"""
        self.assertIsNot(places.__doc__, None,
                         "Places class needs a docstring")
        self.assertTrue(len(places.__doc__) >= 1,
                        "Places class needs a docstring")

    def test_state_class_docstring_users(self):
        """Check for the class docstring in api/v1/views/users.py"""
        self.assertIsNot(users.__doc__, None,
                         "Users class needs a docstring")
        self.assertTrue(len(users.__doc__) >= 1,
                        "Users class needs a docstring")

    def test_state_class_docstring_places_amenities(self):
        """Check for the class docstring in api/v1/views/places_amenities.py"""
        self.assertIsNot(places_amenities.__doc__, None,
                         "PlacesAmenities class needs a docstring")
        self.assertTrue(len(places_amenities.__doc__) >= 1,
                        "PlacesAmenities class needs a docstring")

    def test_state_func_docstrings(self):
        """Check for docstrings in State methods"""
        for func in self.state_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_state_func_docstrings_index(self):
        """Check for docstrings in Index methods"""
        index_f = inspect.getmembers(index, inspect.isfunction)
        for func in index_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_state_func_docstrings_user(self):
        """Check for docstrings in User methods"""
        users_f = inspect.getmembers(users, inspect.isfunction)
        for func in users_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_state_func_docstrings_places(self):
        """Check for docstrings in Places methods"""
        places_f = inspect.getmembers(places, inspect.isfunction)
        for func in places_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_state_func_docstrings_states(self):
        """Check for docstrings in States methods"""
        states_f = inspect.getmembers(test_state, inspect.isfunction)
        for func in states_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_state_func_docstrings_places_reviews(self):
        """Check for docstrings in PlacesReviews methods"""
        places_reviews_f = inspect.getmembers(places_reviews, inspect.isfunction)
        for func in places_reviews_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_state_func_docstrings_places_amenities(self):
        """Check for docstrings in PlacesAmenities methods"""
        places_amenities_f = inspect.getmembers(places_amenities, inspect.isfunction)
        for func in places_amenities_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_state_func_docstrings_cities(self):
        """Check for docstrings in Cities methods"""
        cities_f = inspect.getmembers(cities, inspect.isfunction)
        for func in cities_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_state_func_docstrings_amenities(self):
        """Check for docstrings in Amenities methods"""
        amenities_f = inspect.getmembers(amenities, inspect.isfunction)
        for func in amenities_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))
