#!/usr/bin/python3
"""
This is a docstring for Rectangle
"""

class Rectangle:
        """
        class that defines a rectangle 
        """
        def __init__(self, width=0, height=0):
                self.width = width
                self.height = height

	@property
        def height(self):
                return self.__height

        @height.setter
        def height(self, value):
                if not isinstance(value, int):
                        raise TypeError("width must be an integer")
                if value < 0:
                        raise ValueError("width must be >= 0")
                self._height = value
        @property
        def width(self):
                return self.__width

        @width.setter
        def width(self, value):
                if not isinstance(value, int):
                        raise TypeError("width must be an integer")
                if value < 0:
                        raise ValueError("width must be >= 0")
                self._width = value
