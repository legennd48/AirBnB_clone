#!/usr/bin/python3
"""
Unittest for user module
"""
import os
import unittest
from models.user import User
import models
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """ Test for User Class """

    def setUp(self):
        """set up the test for testing users"""
        FileStorage._FileStorage__file_path = "vault.json"

    def test_args_none(self):
        u = User(None)
        self.assertNotIn(None, u.__dict__.values())

    def test_kwargs_none(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_public(self):
        self.assertEqual(str, type(User().id))

    def test_no_arg(self):
        self.assertEqual(User, type(User()))

    def test_new_instance(self):
        self.assertIn(User(), models.storage.all().values())

    def test_create_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_update_time(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email(self):
        self.assertEqual(str, type(User.email))

    def test_password(self):
        self.assertEqual(str, type(User.password))

    def test_first_name(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        self.assertEqual(str, type(User.last_name))

    def test_multiple_user(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_multiple_user_created(self):
        u1 = User()
        u2 = User()
        self.assertLess(u1.created_at, u2.created_at)

    def test_kwargs(self):
        date_t = datetime.today()
        date_i = date_t.isoformat()
        u = User(id="789", created_at=date_i, updated_at=date_i)
        self.assertEqual(u.id, "789")
        self.assertEqual(u.created_at, date_t)
        self.assertEqual(u.updated_at, date_t)

    def test_args(self):
        date_t = datetime.today()
        date_i = date_t.isoformat()
        date_r = repr(date_t)
        u = User()
        u.id = "851"
        u.created_at = u.updated_at = date_t
        u_str = u.__str__()
        self.assertIn("[User] (851)", u_str)
        self.assertIn("'id': '851'", u_str)
        self.assertIn("'created_at': " + date_r, u_str)
        self.assertIn("'updated_at': " + date_r, u_str)


class TestSave(unittest.TestCase):

    def setUp(self):
        """set up the test for testing users"""
        FileStorage._FileStorage__file_path = "vault.json"

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("vault.json")
        except IOError:
            pass

    def test_save_arg(self):
        u = User()
        with self.assertRaises(TypeError):
            u.save(None)

    def test_save(self):
        u = User()
        update = u.updated_at
        u.save()
        self.assertLess(update, u.updated_at)

    def test_multiple_save(self):
        u = User()
        update = u.updated_at
        u.save()
        update_2 = u.updated_at
        self.assertLess(update, u.updated_at)
        u.save()
        self.assertLess(update_2, u.updated_at)

    def test_save_updated(self):
        u = User()
        u.save()
        u_id = "User." + u.id
        with open("vault.json", "r") as f:
            self.assertIn(u_id, f.read())


class TestUserDict(unittest.TestCase):

    def test_args_none(self):
        u = User()
        with self.assertRaises(TypeError):
            u.to_dict(None)

    def test_mul_dict(self):
        u = User()
        self.assertNotEqual(u.to_dict(), u.__dict__)

    def test_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_dict(self):
        u = User()
        self.assertIn("id", u.to_dict())
        self.assertIn("created_at", u.to_dict())
        self.assertIn("updated_at", u.to_dict())
        self.assertIn("__class__", u.to_dict())

    def test_dict_str(self):
        u = User()
        usr = u.to_dict()
        self.assertEqual(str, type(usr['id']))
        self.assertEqual(str, type(usr["created_at"]))
        self.assertEqual(str, type(usr["updated_at"]))

    def test_dict_end(self):
        date_t = datetime.today()
        date_i = date_t.isoformat()
        u = User()
        u.id = "789"
        u.created_at = u.updated_at = date_t
        Dict = {
            "id": "789",
            "__class__": "User",
            "created_at": date_i,
            "updated_at": date_i,
        }

    def test_dict_arg(self):
        u = User()
        u.name = "Samwell"
        u.number = 74
        self.assertEqual("Samwell", u.name)
        self.assertIn("number", u.to_dict())


if __name__ == "__main__":
    unittest.main()
