#!/usr/bin/python3
"""
This module contains the FlaskTestCase class
"""

from api.v1.app import app
from flask import Flask, make_response, jsonify, json
import unittest
import pprint
import ast
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Testing with FileStorage")
class FlaskTestCase(unittest.TestCase):
    data = {"name": "California"}

    @classmethod
    def setUpClass(cls):
        """Setup for the test cases"""
        cls.app = app

    def test_get_status(self):
        """Test for correct status code in GET request"""
        tester = app.test_client(self)
        response = tester.get('/api/v1/states', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_valid_json(self):
        """Test if the response content type is JSON"""
        tester = app.test_client(self)
        response = tester.get('/api/v1/states', content_type='html/text')
        self.assertEqual(response.content_type, 'application/json')

    def test_post_method(self):
        """Test for correct status code and content type in POST request"""
        tester = app.test_client(self)
        response = tester.post('/api/v1/states', json=self.data)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_post_method(self):
        """Test for data consistency between POST and GET requests"""
        tester = app.test_client(self)
        response = tester.post('/api/v1/states', json=self.data)
        data1 = response.data.decode('UTF-8')
        mydata = ast.literal_eval(data1)
        dic = mydata
        self.assertIn("name", dic)
        self.assertIn("__class__", dic)
        self.assertIn("created_at", dic)
        self.assertIn("id", dic)
        self.assertIn("updated_at", dic)

        response = tester.get('/api/v1/states')
        data1 = response.data.decode('UTF-8')
        mydata = ast.literal_eval(data1)
        dic = mydata[0]
        self.assertIn("name", dic)
        self.assertIn("__class__", dic)
        self.assertIn("created_at", dic)
        self.assertIn("id", dic)
        self.assertIn("updated_at", dic)

    def test_get_method_by_id(self):
        """Test GET request by ID"""
        tester = app.test_client(self)
        response = tester.post('/api/v1/states', json=self.data)
        self.assertEqual(response.status_code, 201)
        data1 = response.data.decode('UTF-8')
        mydata = ast.literal_eval(data1)
        dic_post = mydata

        all_states = tester.get('/api/v1/states')
        self.assertEqual(all_states.status_code, 200)
        data1 = all_states.data.decode('UTF-8')
        all_states = ast.literal_eval(data1)
        dic_get = all_states

        unique_id = dic_get[-1]['id']

        response = tester.get(f'/api/v1/states/{unique_id}')
        self.assertEqual(response.status_code, 200)
        data1 = response.data.decode('UTF-8')
        mydata = ast.literal_eval(data1)
        dic_by_id = mydata

    def test_put_method_by_id(self):
        """Test PUT request by ID"""
        tester = app.test_client(self)
        all_states = tester.get('/api/v1/states')
        self.assertEqual(all_states.status_code, 200)
        data1 = all_states.data.decode('UTF-8')
        all_states = ast.literal_eval(data1)
        dic_get = all_states

        unique_id = dic_get[0]['id']
        updated_data = {"name": "Updating"}
        response = tester.put(f'/api/v1/states/{unique_id}', json=updated_data)
        self.assertEqual(response.status_code, 200)
        data1 = response.data.decode('UTF-8')
        mydata = ast.literal_eval(data1)
        dic_by_id = mydata
        self.assertIn("Updating", dic_by_id['name'])
        self.assertIn("__class__", dic_by_id)
        self.assertIn("created_at", dic_by_id)
        self.assertIn("id", dic_by_id)
        self.assertIn("updated_at", dic_by_id)


if __name__ == "__main__":
    unittest.main()
