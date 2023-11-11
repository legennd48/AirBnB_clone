#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenityInstantiation
    TestAmenitySave
    TestAmenityToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_instantiates(self):
        """ Test no argument instantiation """
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        """ Test new instance stored in object """
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        """ Tests id """
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        """ Tests created_at """
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        """ Tests updated_at """
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        """ Tests name """
        amenity_instance = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amenity_instance.__dict__)

    def test_two_amenities_unique_ids(self):
        """ Test that id is unique """
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_two_amenities_different_created_at(self):
        """ Test that created_at is unique """
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_two_amenities_different_updated_at(self):
        """ Test that updated_at is unique"""
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_str_representation(self):
        """ Tests __str__ """
        current_datetime = datetime.today()
        current_datetime_repr = repr(current_datetime)
        amenity_instance = Amenity()
        amenity_instance.id = "123456"
        amenity_instance.updated_at = current_datetime
        amenity_instance.created_at = current_datetime
        amenity_str = amenity_instance.__str__()
        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertIn("'created_at': " + current_datetime_repr, amenity_str)
        self.assertIn("'updated_at': " + current_datetime_repr, amenity_str)

    def test_args_unused(self):
        """ Test unused args """
        amenity_instance = Amenity(None)
        self.assertNotIn(None, amenity_instance.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Instantiation with kwargs test method"""
        current_datetime = datetime.today()
        current_datetime_iso = current_datetime.isoformat()
        amenity_instance = Amenity(id="345", created_at=current_datetime_iso,
                                   updated_at=current_datetime_iso)
        self.assertEqual(amenity_instance.id, "345")
        self.assertEqual(amenity_instance.created_at, current_datetime)
        self.assertEqual(amenity_instance.updated_at, current_datetime)

    def test_instantiation_with_None_kwargs(self):
        """ Tests instantiation  with none kwargs"""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenitySave(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(self):
        """ set up  """
        try:
            os.rename("vault.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """ tear down or clean up """
        try:
            os.remove("vault.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "vault.json")
        except IOError:
            pass

    def test_one_save(self):
        """ Test save method """
        amenity_instance = Amenity()
        sleep(0.05)
        first_updated_at = amenity_instance.updated_at
        amenity_instance.save()
        self.assertLess(first_updated_at, amenity_instance.updated_at)

    def test_two_saves(self):
        """ Test two save method """
        amenity_instance = Amenity()
        sleep(0.05)
        first_updated_at = amenity_instance.updated_at
        amenity_instance.save()
        second_updated_at = amenity_instance.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amenity_instance.save()
        self.assertLess(second_updated_at, amenity_instance.updated_at)

    def test_save_with_arg(self):
        """ Test save method with arg """
        amenity_instance = Amenity()
        with self.assertRaises(TypeError):
            amenity_instance.save(None)

    def test_save_updates_file(self):
        """ Test save update file """
        amenity_instance = Amenity()
        amenity_instance.save()
        amenity_id = "Amenity." + amenity_instance.id
        with open("vault.json", "r") as f:
            self.assertIn(amenity_id, f.read())


class TestAmenityToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        """ Test to_dict method """
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """ Test to_dict contains ccorrect keys"""
        amenity_instance = Amenity()
        self.assertIn("id", amenity_instance.to_dict())
        self.assertIn("created_at", amenity_instance.to_dict())
        self.assertIn("updated_at", amenity_instance.to_dict())
        self.assertIn("__class__", amenity_instance.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """ Test to_dict contains added attributes"""
        amenity_instance = Amenity()
        amenity_instance.middle_name = "Holberton"
        amenity_instance.my_number = 98
        self.assertEqual("Holberton", amenity_instance.middle_name)
        self.assertIn("my_number", amenity_instance.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """ Test to_dict datetime attributes are strings"""
        amenity_instance = Amenity()
        amenity_dict = amenity_instance.to_dict()
        self.assertEqual(str, type(amenity_dict["id"]))
        self.assertEqual(str, type(amenity_dict["created_at"]))
        self.assertEqual(str, type(amenity_dict["updated_at"]))

    def test_to_dict_output(self):
        """ Test to_dict output"""
        dt = datetime.today()
        amenity_instance = Amenity()
        amenity_instance.id = "987456"
        amenity_instance.created_at = amenity_instance.updated_at = dt
        tdict = {
            'id': '987456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(amenity_instance.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """ Test constrast to_dict"""
        amenity_in = Amenity()
        self.assertNotEqual(amenity_in.to_dict(), amenity_in.__dict__)

    def test_to_dict_with_arg(self):
        """ Test to_dict with args """
        amenity_instance = Amenity()
        with self.assertRaises(TypeError):
            amenity_instance.to_dict(None)


if __name__ == "__main__":
    unittest.main()
