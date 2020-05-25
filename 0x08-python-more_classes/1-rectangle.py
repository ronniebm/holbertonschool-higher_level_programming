#!/usr/bin/python3
"""Defining a new class"""


class Rectangle:
    """an empty class Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # get width
    @property
    def width(self):
        return self.__width

    # get height
    @property
    def height(self):
        return self.__height

    # width property setter
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    # heigth property setter
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('heigth must be an integer')
        elif value < 0:
            raise ValueError('heigth must be >= 0')
        self.__height = value