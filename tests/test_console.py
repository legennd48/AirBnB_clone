#!/usr/bin/python3
'''
unittest for console.py
'''
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.engine.file_storage import FileStorage
from models import storage
from io import StringIO
import os
import json
import console
import tests


class TestHBNB_prompt(unittest.TestCase):
    '''
    Test cases for HBNBCommand prompt and emptyline methods
    '''

    def testprompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBcreate(unittest.TestCase):
    '''
    Test cases for HBNBCommand create method
    '''

    @classmethod
    def setUp(self):
        try:
            os.rename("vault.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_create_missing_class(self):
        '''
        Test create method with missing class name
        '''
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_invalid_class(self):
        '''
        Test create method with invalid class name
        '''
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_create_object(self):
        '''
        Test create method with valid class name
        '''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "User.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "City.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Place.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Review.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())


class TestHBNBOtherCommands(unittest.TestCase):
    '''
    Test cases for other commands in HBNBCommand class
    '''

    @classmethod
    def setUpClass(cls):
        HBNBCommand().onecmd("create BaseModel")
        HBNBCommand().onecmd("create User")

    def test_show(self):
        '''
        Test show command
        '''
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel")
            self.assertIn("BaseModel", output.getvalue().strip())

    def test_destroy(self):
        '''
        Test destroy command
        '''
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual("** no instance found **", output.getvalue().strip())

    def test_all(self):
        '''
        Test all command
        '''
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn("BaseModel", output.getvalue().strip())

    def test_update(self):
        '''
        Test update command
        '''
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel {} name 'new_name'".format(
                list(storage.all("BaseModel").keys())[0]))
            self.assertEqual("** no instance found **", output.getvalue().strip())

    def test_count(self):
        '''
        Test count command
        '''
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("count BaseModel")
            self.assertEqual("1", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
