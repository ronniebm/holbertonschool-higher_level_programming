#!/usr/bin/python3
"""13-student.py module"""


class Student:
    """
    a student class.

    Attributes:
    -----------
    first_name (attrib) -- student's first name.
    last_name (attrib) -- student's last name.
    age (attrib) -- student's age.
    """
    def __init__(self, first_name, last_name, age):
        """Instance constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation
        of an student instance.
        """
        new_dict = {}
        if attrs is not None:
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all the attributes
        of an instance.
        """
        for key, value in json.items():
            self.__dict__[key] = value
