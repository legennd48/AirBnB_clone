#!/usr/bin/python3
'''
Module: 8. First User
class user that inherits from BaseModel
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''User class which inherits from BaseModel'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
