#!/usr/bin/python3
"""Defining a new class"""


class Rectangle:
    """
     class Rectangle.

     Arguments:
     ----------
        width  {int} -- [Rectangle's width]
        height {int} -- [Rectangle's height]

     Raises:
     -------
        TypeError:  [width != int, height != int]
        ValueError: [width < 0,    height < 0]

     Methods:
     -------
        area(self) -- [returns a Rectangle's area]
        perimeter(self) -- [returns a Rectangle's perimeter]

    """
    # init method, width, height.
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # get width.
    @property
    def width(self):
        return self.__width

    # get height.
    @property
    def height(self):
        return self.__height

    # width property setter.
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    # height property setter.
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    # Rectangle's area method.
    def area(self):
        return (self.__width * self.__height)

    # Rectangle's perimeter method.
    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))
