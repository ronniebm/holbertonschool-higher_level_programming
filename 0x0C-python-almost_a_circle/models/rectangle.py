#!/usr/bin/python3
""" rectangle.py module"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class.

    Inheritance: from Base Class.
    -----------
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor.

        Arguments:
        ----------
        width [int] -- width of class.
        height [int] -- height of class.
        x [int] -- x of class, default = 0.
        y [int] -- y of class, default = 0.
        id [int] -- instance counter.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, val):
        """setter method for width"""
        if type(val) is not int:
            raise TypeError('width must be an integer')
        elif val <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = val

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, val):
        """setter method for height"""
        if type(val) is not int:
            raise TypeError('height must be an integer')
        elif val <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = val

    @property
    def x(self):
        """getter method for height"""
        return self.__x

    @x.setter
    def x(self, val):
        """setter method for x"""
        if type(val) is not int:
            raise TypeError('x must be an integer')
        elif val < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = val

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, val):
        """setter method for y"""
        if type(val) is not int:
            raise TypeError('y must be an integer')
        elif val < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = val

    def area(self):
        """
        area: calculates rectangle's area.

        Return:
        -------
        val [int] -- area of a rectangle.
        """
        return (self.__width * self.__height)

    def display(self):
        """
        display:
        """
        for i in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """overriding the __str__ method"""
        h = self.__height
        w = self.__width
        x = self.__x
        y = self.__y
        _id = self.id
        return("[Rectangle] (<{0}>) <{1}>/<{2}> - <{3}>/<{4}>".format(
            _id, x, y, w, h))
