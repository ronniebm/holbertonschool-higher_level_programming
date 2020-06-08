#!/usr/bin/python3
""" base.py module """
import json


class Base():
    """ My base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string static method"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
