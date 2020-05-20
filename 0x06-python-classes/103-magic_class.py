#!/usr/bin/python3

'''class definitions'''


class Magic:
    '''defining class: Square'''

    # initializing method
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.radius = None

    # defining area method
    def area(self):
        return self.radius ** 2 * 3.14

    # defining circumference method
    def circumference(self):
        return self.radius * 2 * 3.14
