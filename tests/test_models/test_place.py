#!/usr/bin/python3

"""
    This module tests city class
"""


import unittest
from models.user import User
from models.city import City
from models.place import Place
from datetime import datetime


class TestPlaceClass(unittest.TestCase):
    """
        Test Suite of Place Class
    """
    def setUp(self):
        """ Set up a Place Class instance """
        self.place_instance = Place()

    def test_attributes_inherited_from_BaseModel(self):
        """ Tests that place has BaseModel attributes"""
        self.assertTrue(hasattr(self.place_instance, "id"))
        self.assertTrue(hasattr(self.place_instance, "created_at"))
        self.assertTrue(hasattr(self.place_instance, "updated_at"))

    def test_default_values(self):
        """ Tests that default value of name set properly """
        self.assertEqual(self.place_instance.name, "")
        self.assertEqual(self.place_instance.amenity_ids, [])
        self.assertEqual(self.place_instance.city_id, "")
        self.assertEqual(self.place_instance.user_id, "")
        self.assertEqual(self.place_instance.description, "")
        self.assertEqual(self.place_instance.number_rooms, 0)
        self.assertEqual(self.place_instance.number_bathrooms, 0)
        self.assertEqual(self.place_instance.max_guest, 0)
        self.assertEqual(self.place_instance.price_by_night, 0)
        self.assertEqual(self.place_instance.latitude, 0.0)
        self.assertEqual(self.place_instance.longitude, 0.0)

    def test_name_attribute(self):
        """ Tests name attribute """
        self.place_instance.name = "New Place"
        self.assertEqual(self.place_instance.name, "New Place")

    def test_created_at_and_updated_at_are_datetime_objects(self):
        """ Test that created_at and updated_at are datetime objects"""
        self.assertIsInstance(self.place_instance.created_at, datetime)
        self.assertIsInstance(self.place_instance.updated_at, datetime)

    def test_save_method_inherited_from_BaseModel(self):
        """ Tests that save updates 'updated_at' """
        prev_updated_at = self.place_instance.updated_at
        self.place_instance.save()
        curr_updated_at = self.place_instance.updated_at
        self.assertNotEqual(prev_updated_at, curr_updated_at)

    def test_to_dict_method_inherited_from_BaseModel(self):
        """ Tests that to_dict returns a dictionary representation of
            of city Instance
        """
        dict_rep = self.place_instance.to_dict()
        created_at_str = dict_rep["created_at"]
        updated_at_str = dict_rep["updated_at"]

        self.assertIsInstance(dict_rep, dict)
        self.assertIn("__class__", dict_rep)
        self.assertEqual(dict_rep["__class__"], "Place")

        self.assertIsInstance(created_at_str, str)
        self.assertIsInstance(updated_at_str, str)

        try:
            datetime.fromisoformat(created_at_str)
            datetime.fromisoformat(updated_at_str)

        except ValueError:
            self.fail("created_at and updated_at must be in ISO format")


if "__name__" == "__main__":
    unittest.main()
