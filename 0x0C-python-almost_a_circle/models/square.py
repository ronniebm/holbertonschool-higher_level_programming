#!/usr/bin/python3
""" square.py module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Rectangle Rectangle.

    Inheritance: from Base Rectangle.
    -----------
    """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for width"""
        return self.__size

    @size.setter
    def size(self, val):
        """setter method for width"""
        if type(val) is not int:
            raise TypeError('width must be an integer')
        elif val <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__size = val

    def __str__(self):
        """overriding the __str__ method"""
        s = self.size
        x = self.x
        y = self.y
        _id = self.id
        return("[Square] ({0}) {1}/{2} - {3}".format(_id, x, y, s))
