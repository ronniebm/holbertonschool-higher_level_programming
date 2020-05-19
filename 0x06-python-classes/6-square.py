#!/usr/bin/python3
'''class definitions'''


class Square:
    '''defining class: Square'''

    # initializing method
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    # size property
    @property
    def size(self):
        return self.__size

    # size setter property
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    # position property
    @property
    def position(self):
        return self.__position

    # position setter property
    @position.setter
    def position(self, value):
        message = 'position must be a tuple of 2 positive integers'
        if type(value) != tuple or len(value) != 2:
            raise TypeError(message)

        for items in value:
            if type(items) != int or items < 0:
                raise TypeError(message)

        self.__position = value

    # area calculation method
    def area(self):
        return self.__size ** 2

    # size print method
    def my_print(self):
        size = self.__size
        lines = self.__position[1]
        spaces = self.__position[0]

        if size == 0:
            print()

        for newlines in range(lines):
            print()

        for row in range(size):
            print((' ' * spaces) + ('#' * size))
