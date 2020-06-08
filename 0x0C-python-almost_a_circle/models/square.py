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

    def update(self, *args, **kwargs):
        """update method"""
        _len = len(args)
        if not args:
            if kwargs.get('id') is not None:
                self.id = kwargs.get('id')
            if kwargs.get('size') is not None:
                self.size = kwargs.get('size')
            if kwargs.get('x') is not None:
                self.x = kwargs.get('x')
            if kwargs.get('y') is not None:
                self.y = kwargs.get('y')
        else:
            if _len >= 1 and args[0] is not None:
                self.id = args[0]
            if _len >= 2 and args[1] is not None:
                self.size = args[1]
            if _len >= 3 and args[2] is not None:
                self.x = args[2]
            if _len >= 4 and args[3] is not None:
                self.y = args[3]