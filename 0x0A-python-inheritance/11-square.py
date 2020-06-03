#!/usr/bin/python3
"""11-square.py module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits
    from class 'Rectangle'

    Attributes:
    ----------
    size  {int} -- [Square's size]

    """
    def __init__(self, size):
        """
        constructor with private size attribute.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        print function for square.
        """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
