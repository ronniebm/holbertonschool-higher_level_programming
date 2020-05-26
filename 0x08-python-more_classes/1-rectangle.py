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

    """

    def __init__(self, width=0, height=0):
        """
        initialization:
        ---------------
        width = 0
        height = 0
        """
        self.width = width
        self.height = height

    # get width
    @property
    def width(self):
        """retrieves Rectangle Width"""
        return self.__width

    # get height
    @property
    def height(self):
        """Retrieves Rectangle Height"""
        return self.__height

    # width property setter
    @width.setter
    def width(self, value):
        """Set value for Rectangle's width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    # heigth property setter
    @height.setter
    def height(self, value):
        """Set value for Rectangle's height"""
        if type(value) != int:
            raise TypeError('heigth must be an integer')
        elif value < 0:
            raise ValueError('heigth must be >= 0')
        self.__height = value
