#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""8-rectangle.py module"""


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits
    from class 'BaseGeometry'

    Arguments:
    ----------
    width  {int} -- [Rectangle's width]
    height {int} -- [Rectangle's height]

    """

    def __init__(self, width, height):
        """
        private attributes width and height,
        and validating if they are ints.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
