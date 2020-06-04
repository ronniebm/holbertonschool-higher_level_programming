#!/usr/bin/python3
"""11-student.py module"""


class Student:
    """
    a student class.

    Attributes:
    -----------
    first_name (attrib) -- student's first name.
    last_name (attrib) -- student's last name.
    age (attrib) -- student's age.
    "xs""
    def __init__(self, first_name, last_name, age):
        """Instance constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation"""
        return self.__dict__
