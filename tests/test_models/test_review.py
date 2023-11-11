#!/usr/bin/python3

"""
    This module tests State class
"""


import unittest
from models.place import Place
from models.user import User
from models.review import Review
from datetime import datetime


class TestReviewClass(unittest.TestCase):
    """
        Test Suite of Review Class
    """
    def setUp(self):
        """ Set up a Review Class instance """
        self.review_instance = Review()

    def test_attributes_inherited_from_BaseModel(self):
        """ Tests that state has BaseModel attributes"""
        self.assertTrue(hasattr(self.review_instance, "id"))
        self.assertTrue(hasattr(self.review_instance, "created_at"))
        self.assertTrue(hasattr(self.review_instance, "updated_at"))

    def test_default_values(self):
        """ Tests that default value of name set properly """
        self.assertEqual(self.review_instance.text, "")
        self.assertEqual(self.review_instance.place_id, "")
        self.assertEqual(self.review_instance.user_id, "")

    def test_text_attribute(self):
        """ Tests text attribute """
        self.review_instance.text = "Random text"
        self.assertEqual(self.review_instance.text, "Random text")

    def test_created_at_and_updated_at_are_datetime_objects(self):
        """ Test that created_at and updated_at are datetime objects"""
        self.assertIsInstance(self.review_instance.created_at, datetime)
        self.assertIsInstance(self.review_instance.updated_at, datetime)

    def test_save_method_inherited_from_BaseModel(self):
        """ Tests that save updates 'updated_at' """
        prev_updated_at = self.review_instance.updated_at
        self.review_instance.save()
        curr_updated_at = self.review_instance.updated_at
        self.assertNotEqual(prev_updated_at, curr_updated_at)

    def test_to_dict_method_inherited_from_BaseModel(self):
        """ Tests that to_dict returns a dictionary representation of
            of State Instance
        """
        dict_rep = self.review_instance.to_dict()
        created_at_str = dict_rep["created_at"]
        updated_at_str = dict_rep["updated_at"]

        self.assertIsInstance(dict_rep, dict)
        self.assertIn("__class__", dict_rep)
        self.assertEqual(dict_rep["__class__"], "Review")

        self.assertIsInstance(created_at_str, str)
        self.assertIsInstance(updated_at_str, str)

        try:
            datetime.fromisoformat(created_at_str)
            datetime.fromisoformat(updated_at_str)

        except ValueError:
            self.fail("created_at and updated_at must be in ISO format")


if "__name__" == "__main__":
    unittest.main()
