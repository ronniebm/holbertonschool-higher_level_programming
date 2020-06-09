#!/usr/bin/python3
""" base.py module """
import json
import csv
from os import path


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

    @classmethod
    def load_from_file(cls):
        """
        load_from_file method:
        ----------------------
        a method that returns a list of instances.
        """

        filename = cls.__name__ + ".json"
        newlist = []
        if cls is None:
            return newlist
        try:
            with open(filename, mode="r", encoding='utf-8') as Myfile:
                newlist = cls.from_json_string(Myfile.read())
            for item in range(len(newlist)):
                newlist[item] = cls.create(**newlist[item])
        except Exception:
            pass
        return newlist


    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        writes a object's list string representation
        into a CVS file
        """
        with open(cls.__name__ + ".csv", "w", newline='') as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']

            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            if list_objs is not None:
                for model in list_objs:
                    writer.writerow(model.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        reads from a CVS file an object's list
        string representation.
        """
        if path.exists(cls.__name__ + ".csv") is False:
            return []

        with open(cls.__name__ + ".csv", "r", newline='') as f:
            listofinstances = []
            reader = csv.DictReader(f)
            for row in reader:
                for key, value in row.items():
                    row[key] = int(value)
                listofinstances.append(cls.create(**row))

        return listofinstances
