#!/usr/bin/python3
""" rectangle.py module"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class.

    Inheritance: from Base Class.
    -----------
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor.

        Arguments:
        ----------
        width [int] -- width of class.
        height [int] -- height of class.
        x [int] -- x of class, default = 0.
        y [int] -- y of class, default = 0.
        id [int] -- instance counter.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, val):
        """setter method for width"""
        self.__width = val

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, val):
        """setter method for height"""
        self.__height = val

    @property
    def x(self):
        """getter method for height"""
        return self.__x

    @x.setter
    def x(self, val):
        """setter method for x"""
        self.__x = val

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, val):
        """setter method for y"""
        self.__y = val
