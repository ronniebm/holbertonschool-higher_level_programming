#!/usr/bin/python3
'''Defininf a new class'''


class Square:
    '''a class Square that defines a square'''
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''defining area method'''
        size = self.__size
        return size * size
