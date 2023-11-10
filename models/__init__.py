#!/usr/bin/python3
"""magic method to to create a unique FileStorage instance
for all models in directory
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
