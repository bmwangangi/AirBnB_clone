#!/usr/bin/python3

"""creates aclass."""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """class that that serializes instances to a JSON file."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """class that returns models dict"""
        return self.__objects

    def new(self, obj):
        """function method that sets objects with key."""
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """func method to serialize object to JSON file path."""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """func method to deserialize JSON file."""
        from models.base_model import BaseModel
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                try:
                    objs = json.load(f)
                except json.JSONDecodeError:
                    objs = {}
            for k, v in objs.items():
                class_name = v['__class__']
                if class_name == 'BaseModel':
                    self.__objects[k] = BaseModel(**v)
                elif class_name == 'User':
                    self.__objects[k] = User(**v)
                elif class_name == 'State':
                    self.__objects[k] = State(**v)
                elif class_name == 'City':
                    self.__objects[k] = City(**v)
                elif class_name == 'Amenity':
                    self.__objects[k] = Amenity(**v)
                elif class_name == 'Place':
                    self.__objects[k] = Place(**v)
                elif class_name == 'Review':
                    self.__objects[k] = Review(**v)s