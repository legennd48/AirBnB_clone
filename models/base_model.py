#!/usr/bin/python3

"""
    This module supplies the BaseModel class.
"""


import uuid
from datetime import datetime


class BaseModel:
    """
        This class acts as the base class
        for other classes/models.

        Attributes
        ----------
            id (string): a uuid string
            created_at (datetime): a datetime value
            updated_at (datetime): a datetime value

        Methods
        -------
            save: updates "updated_at" attribute
            to_dict: converts instances to dictionary representation
    """
    def __init__(self, *args, **kwargs):
        """
            This is the constructor method
            for the BaseModel class. 
        """ 
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            self.id = kwargs.get("id", self.id)
            self.created_at = datetime.fromisoformat(kwargs.get("created_at", self.created_at))
            self.updated_at = datetime.fromisoformat(kwargs.get("updated_at", self.updated_at))

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.created_at = datetime.fromisoformat(args[1])
            if len(args) >= 3:
                self.updated_at = datetime.fromisoformat(args[2])
            

    def __str__(self):
        """
            This method provides the string representaion for
            an instance of the BaseModel class.
        """
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            This method updates the instance of the
            BaseModel class.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
            This method provides the dictionary
            representaionof an instance of the
            BaseModel class.
        """
        dict_rep = {
            "__class__": type(self).__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
        
        for key, value in self.__dict__.items():
            if key not in {"created_at", "updated_at"}:
                dict_rep[key] = value

        return dict_rep
        