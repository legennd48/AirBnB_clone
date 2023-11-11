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
        self.assertIsInstance(self.base_model.id, str, "id should be a string")
    
    def test_created_at(self):
        """ Tests that created_at is datetime """
        self.assertIsInstance(self.base_model.created_at, datetime, "created_at should be a datetime")

    def test_updated_at(self):
        """ Tests that updated_at is datetime """
        self.assertIsInstance(self.base_model.updated_at, datetime, "updated_at should be a datetime")

    def test_save_method(self):
        """ Tests that save updates 'updated_at' """
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        curr_updated_at = self.base_model.updated_at
        self.assertNotEqual(prev_updated_at, curr_updated_at, "save method should update updated_at")

    def test_to_dict_method(self):
        """ Tests that to_dict returns a dictionary representation of
            of BaseModel Instance
        """
        dict_rep = self.base_model.to_dict()
        created_at_str = dict_rep["created_at"]
        updated_at_str = dict_rep["updated_at"]

        self.assertIsInstance(dict_rep, dict, "to_dict should return a dictionary")
        self.assertIn("__class__", dict_rep, "dict_rep should contain '__class__' key")
        self.assertEqual(dict_rep["__class__"], "BaseModel", "'__class__' should be the class name")

        self.assertIsInstance(created_at_str, str, "created_at should be a string")
        self.assertIsInstance(updated_at_str, str, "updated_at should be a string")

        try:
            datetime.fromisoformat(created_at_str)
            datetime.fromisoformat(updated_at_str)

        except ValueError:
            self.fail("created_at and updated_at must be in ISO format")

if "__name__" == "__main__":
    unittest.main()