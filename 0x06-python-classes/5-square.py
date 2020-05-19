#!/usr/bin/python3
'''class definitions'''


class Square:
    '''defining class: Square'''

    # initializing method
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

    # area calculation method
    def area(self):
        return self.__size ** 2

    # size print method
    def my_print(self):
        size = self.__size

        if size == 0:
            print()

        for row in range(size):
            print('#' * size)
