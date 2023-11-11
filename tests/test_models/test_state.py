#!/usr/bin/python3

"""
    This module tests State class
"""


import unittest
from models.state import State
from datetime import datetime


class TestStateClass(unittest.TestCase):
    """
        Test Suite of State Class
    """
    def setUp(self):
        """ Set up a State Class instance """
        self.state_instance = State()

    def test_attributes_inherited_from_BaseModel(self):
        """ Tests that state has BaseModel attributes"""
        self.assertTrue(hasattr(self.state_instance, "id"))
        self.assertTrue(hasattr(self.state_instance, "created_at"))
        self.assertTrue(hasattr(self.state_instance, "updated_at"))

    def test_default_values(self):
        """ Tests that default value of name set properly """
        self.assertEqual(self.state_instance.name, "")

    def test_name_attribute(self):
        """ Tests name attribute """
        self.state_instance.name = "Lagos"
        self.assertEqual(self.state_instance.name, "Lagos")

    def test_created_at_and_updated_at_are_datetime_objects(self):
        """ Test that created_at and updated_at are datetime objects"""
        self.assertIsInstance(self.state_instance.created_at, datetime)
        self.assertIsInstance(self.state_instance.updated_at, datetime)

    def test_save_method_inherited_from_BaseModel(self):
        """ Tests that save updates 'updated_at' """
        prev_updated_at = self.state_instance.updated_at
        self.state_instance.save()
        curr_updated_at = self.state_instance.updated_at
        self.assertNotEqual(prev_updated_at, curr_updated_at)

    def test_to_dict_method_inherited_from_BaseModel(self):
        """ Tests that to_dict returns a dictionary representation of
            of State Instance
        """
        dict_rep = self.state_instance.to_dict()
        created_at_str = dict_rep["created_at"]
        updated_at_str = dict_rep["updated_at"]

        self.assertIsInstance(dict_rep, dict)
        self.assertIn("__class__", dict_rep)
        self.assertEqual(dict_rep["__class__"], "State")

        self.assertIsInstance(created_at_str, str)
        self.assertIsInstance(updated_at_str, str)

        try:
            datetime.fromisoformat(created_at_str)
            datetime.fromisoformat(updated_at_str)

        except ValueError:
            self.fail("created_at and updated_at must be in ISO format")


if "__name__" == "__main__":
    unittest.main()
