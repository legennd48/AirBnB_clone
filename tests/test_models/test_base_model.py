#!/usr/bin/python3


"""
    This module tests BaseModel class
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        Test Suite of BaseModel class
    """
    def setUp(self):
        """
            Set up a BaseModel instance
        """
        self.base_model = BaseModel()

    def test_id(self):
        """ Tests that id is a string """
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        """ Tests that created_at is datetime """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """ Tests that updated_at is datetime """
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        """ Tests that save updates 'updated_at' """
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        curr_updated_at = self.base_model.updated_at
        self.assertNotEqual(prev_updated_at, curr_updated_at)

    def test_to_dict_method(self):
        """ Tests that to_dict returns a dictionary representation of
            of BaseModel Instance
        """
        dict_rep = self.base_model.to_dict()
        created_at_str = dict_rep["created_at"]
        updated_at_str = dict_rep["updated_at"]

        self.assertIsInstance(dict_rep, dict)
        self.assertIn("__class__", dict_rep)
        self.assertEqual(dict_rep["__class__"], "BaseModel")

        self.assertIsInstance(created_at_str, str)
        self.assertIsInstance(updated_at_str, str)

        try:
            datetime.fromisoformat(created_at_str)
            datetime.fromisoformat(updated_at_str)

        except ValueError:
            self.fail("created_at and updated_at must be in ISO format")

    def test_recreate_instance_from_dict(self):
        """ Tests the creation of instance from dictionary """
        dict_rep = self.base_model.to_dict()

        # Create a new instance from the dictionary
        recreated_instance = BaseModel(**dict_rep)

        # Verify the properties of the recreated instance
        self.assertIsInstance(recreated_instance.id, str)
        self.assertIsInstance(recreated_instance.created_at, datetime)
        self.assertIsInstance(recreated_instance.updated_at, datetime)
        self.assertNotIn("__class__", recreated_instance.__dict__)


if "__name__" == "__main__":
    unittest.main()
