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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file class method.
        --------------------------
        writes the JSON string representation of
        list_objs to a file.

        Arguments:
        ---------
        list_objs [list] -- a list of instances who
        inherits of Base.
        """
        file = cls.__name__ + '.json'

        with open(file, mode='w', encoding='utf-8') as myfile:
            if list_objs is None:
                myfile.write("[]")
            else:
                l_dict = []
                for i in range(len(list_objs)):
                    l_dict.append(list_objs[i].to_dictionary())
                myfile.write(Base.to_json_string(l_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_strinc class method.
        -----------------------------

        Arguments:
        ----------
        json_string [str] -- is a string representing a
        list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create method:
        --------------
        returns an instance with all attributes already set:
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(8, 9)
            else:
                new = cls(5)
            new.update(**dictionary)
            return new
