#!/usr/bin/python3
"""Defines FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Method to represent an abstracted storage engine.
    Attributes:
        __file_path (str): File name to save objects to.
        __objects (dict): dictionary of the instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method to return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in-objects objct with key <objct_class_name>.id"""
        ocname = objct.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, objct.id)] = objct

    def save(self):
        """Serialize __objects to the JSON file_path."""
        odict = FileStorage.__objects
        objdict = {objct: r_dict[objct]_dict() for objct in r_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj, f)

    def reload(self):
        """Deserialize the JSON file_path to objects if exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj = json.load(f)
                for o in obj.values():
                    cls_wrd = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_wrd)(**o))
        except FileNotFoundError:
            return