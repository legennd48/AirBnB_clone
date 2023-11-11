#!/usr/bin/python3

"""
    This module tests city class
"""


import unittest
from models.state import State
from models.city import City
from datetime import datetime


class TestCityClass(unittest.TestCase):
    """
        Test Suite of City Class
    """
    def setUp(self):
        """ Set up a City Class instance """
        self.city_instance = City()

    def test_attributes_inherited_from_BaseModel(self):
        """ Tests that city has BaseModel attributes"""
        self.assertTrue(hasattr(self.city_instance, "id"))
        self.assertTrue(hasattr(self.city_instance, "created_at"))
        self.assertTrue(hasattr(self.city_instance, "updated_at"))

    def test_default_values(self):
        """ Tests that default value of name set properly """
        self.assertEqual(self.city_instance.name, "")
        self.assertEqual(self.city_instance.state_id, "")

    def test_name_attribute(self):
        """ Tests name attribute """
        self.city_instance.name = "New City"
        self.assertEqual(self.city_instance.name, "New City")

    def test_created_at_and_updated_at_are_datetime_objects(self):
        """ Test that created_at and updated_at are datetime objects"""
        self.assertIsInstance(self.city_instance.created_at, datetime)
        self.assertIsInstance(self.city_instance.updated_at, datetime)

    def test_save_method_inherited_from_BaseModel(self):
        """ Tests that save updates 'updated_at' """
        prev_updated_at = self.city_instance.updated_at
        self.city_instance.save()
        curr_updated_at = self.city_instance.updated_at
        self.assertNotEqual(prev_updated_at, curr_updated_at)

    def test_to_dict_method_inherited_from_BaseModel(self):
        """ Tests that to_dict returns a dictionary representation of
            of city Instance
        """
        dict_rep = self.city_instance.to_dict()
        created_at_str = dict_rep["created_at"]
        updated_at_str = dict_rep["updated_at"]

        self.assertIsInstance(dict_rep, dict)
        self.assertIn("__class__", dict_rep)
        self.assertEqual(dict_rep["__class__"], "City")

        self.assertIsInstance(created_at_str, str)
        self.assertIsInstance(updated_at_str, str)

        try:
            datetime.fromisoformat(created_at_str)
            datetime.fromisoformat(updated_at_str)

        except ValueError:
            self.fail("created_at and updated_at must be in ISO format")


if "__name__" == "__main__":
    unittest.main()
