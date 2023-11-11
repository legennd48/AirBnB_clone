#!/usr/bin/python3
'''
Module: 5. Store first object
defines the filestorage class that serializes instances to a JSON file
and deserializes JSON file to instances:
'''

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class works as a file storage engine.

    Attributes:
        __file_path (str): Path to target file where new objects are saved.
        __objects (dict): A dictionary where all objects are stored.
    """
    __file_path = "vault.json"
    __objects = {}

    def all(self):
        ''' returns the dictionary __objects '''
        dictObj = FileStorage.__objects
        return dictObj

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        dictObj = FileStorage.__objects
        name = obj.__class__.__name__
        formatT = f"{name}.{obj.id}"
        dictObj[formatT] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        dictObj = FileStorage.__objects
        objDict = {}
        for k, v in dictObj.items():
            objDict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as jsonFile:
            json.dump(objDict, jsonFile)

    def reload(self):
        ''' deserializes the JSON file to __objects'''
        try:
            with open(FileStorage.__file_path) as f:
                target = json.load(f)
                for val in target.values():
                    clsName = val["__class__"]
                    del val["__class__"]
                    self.new(eval(clsName)(**val))
        except FileNotFoundError:
            pass
