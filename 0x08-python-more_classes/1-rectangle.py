#!/usr/bin/python3
"""
This is a docstring for class Rectangle
"""

class Rectangle:
        """
        class that defines a rectangle 
        """
        def __init__(self, width=0, height=0):
                self.width = a
                self.height = b

        @property
        def width(self):
                return self.__width

        @property.setter
        def width(self, value):
                if not isinstance(width, int):
                        raise TypeError("width must be an integer")
                if width < 0:
                        raise ValueError("width must be >= 0")
                self._width = value
        @property
        def height(self):
                return self.__height

        @property.setter
        def height(self, value):
                if not isinstance(width, int):
                        raise TypeError("width must be an integer")
                if height < 0:
                        raise ValueError("width must be >= 0")
                self._height = value
