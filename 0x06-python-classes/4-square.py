#!/usr/bin/python3
'''Defining a new class'''


class Square:
    '''class Square'''

    # initializing size
    def __init__(self, size=0):
        self.__size = size

    # size property
    @property
    def size(self):
        return self.__size

    # setter property
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    # method
    def area(self):
        return self.__size ** 2
