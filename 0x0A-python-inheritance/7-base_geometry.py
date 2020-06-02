#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry():
    """
    BaseGeometry class.

    Raises:
    -------
    Exception: area(self) method not implemented.
    TypeError:
    ValueError:

    Methods:
    -------
    area(self) -- [not implemented]
    integer_validator(self, name, value) -- [checks value]
    """

    def area(self):
        """
        area: not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        integer_validador: check 'int' type and value > 0.
        """
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
