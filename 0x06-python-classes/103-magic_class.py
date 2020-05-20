#!/usr/bin/python3


class MagicClass:
    '''defining class: MagicClass'''

    # initializing method
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    # defining area method
    def area(self, radius):
        return self.__radius ** 2 * 3.141592653589793

    # defining circumference method
    def circumference(self, radius):
        return self.__radius * 2 * 3.141592653589793
