#!/usr/bin/python3
"""
empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    defines a rectangle
    """

    def __init__(self, width=None, height=None):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if isinstance(value, (int)):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer") 

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if isinstance(value, (int)):
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")
