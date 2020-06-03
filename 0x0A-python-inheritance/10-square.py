#!/usr/bin/python3
"""10-square.py module"""


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

    def area(self):
        """
        area: returns the square's area.
        """
        return (self.__size ** 2)
