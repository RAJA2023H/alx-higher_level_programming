#!/usr/bin/python3
"""
empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    defines a rectangle
    """

    def __init__(self, width=None, height=None):
        """
        initializes the instance

        width: width of the rectangle
        height: height of the rectangle

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        returns the value of the width


        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        defines the width
        value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero


        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer") 

    @property
    def height(self):
        """
        returns the value of the height


        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        defines the height
        value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero


        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")
