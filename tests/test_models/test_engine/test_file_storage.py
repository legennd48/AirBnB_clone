#!/usr/bin/python3
'''
unittest for file_storage module
'''
import unittest
import json
import models
import os
from datetime import datetime
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place


class Test_FileStorage(unittest.TestCase):
    def setUp(self):
        '''Create an instance of FileStorage for testing'''
        FileStorage._FileStorage__file_path = "vault.json"

    def test_no_arguments(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_instantiation(self):
        self.assertEqual(FileStorage, type(models.storage))

    def test_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

class Test_FileStorage_methods(unittest.TestCase):
    @classmethod
    def setUp(self):
        try:
            os.rename("vault.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("vault.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "vault.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_no_arguments(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arguments(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_all_classes(self):
        Bm = BaseModel()
        models.storage.new(Bm)
        models.storage.new(Amenity())
        models.storage.new(Place())
        models.storage.new(User())
        models.storage.new(State())
        models.storage.new(Review())
        models.storage.new(City())
        self.assertIn("BaseModel." + Bm.id, models.storage.all().keys())
        self.assertIn(Bm, models.storage.all().values())
        self.assertIn(Bm, models.storage.all().values())
        self.assertIn("Amenity." + Amenity().id, models.storage.all().keys())
        self.assertIn(Amenity(), models.storage.all().values())
        self.assertIn("Place." + Place().id, models.storage.all().keys())
        self.assertIn(Place(), models.storage.all().values())
        self.assertIn("User." + User().id, models.storage.all().keys())
        self.assertIn(User(), models.storage.all().values())
        self.assertIn("State." + State().id, models.storage.all().keys())
        self.assertIn(State(), models.storage.all().values())
        self.assertIn("Review." + Review().id, models.storage.all().keys())
        self.assertIn(Review(), models.storage.all().values())
        self.assertIn("City." + City().id, models.storage.all().keys())
        self.assertIn(City(), models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("vault.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)


if __name__ == "__main__":
    unittest.main()
