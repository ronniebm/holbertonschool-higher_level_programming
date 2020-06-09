#!/usr/bin/python3
""" base.py module """
import json
import csv


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
        filename = cls.__name__ + ".csv"

        with open(filename, mode='w', encoding='utf-8') as file:
            string = csv.writer(file)

            if cls.__name__ is "Square":
                for i in list_objs:
                    string.writerow([i.id, i.size, i.x, i.y])
            elif cls.__name__ is "Rectangle":
                for i in list_objs:
                    string.writerow([i.id, i.width, i.height, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        reads from a CVS file an object's list
        string representation.
        """
        filename = cls.__name__ + ".csv"
        mylist = []

        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                read = csv.reader(file)
                for i in read:
                    if cls.__name__ is "Square":
                        dict1 = {"id": int(i[0]), "size": int(i[1]),
                                "x": int(i[2]), "y": int(i[3])}
                    elif cls.__name__ is "Rectangle":
                        dict1 = {"id": int(i[0]), "width": int(i[1]),
                                "height": int(i[2]), "x": int(i[3]),
                                "y": int(i[4])}
                    mylist.append(cls.create(**dict1))
            return mylist
        except:
            return []