#!/usr/bin/python3

# from models.base_model import BaseModel
'''Initializes the package'''

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
