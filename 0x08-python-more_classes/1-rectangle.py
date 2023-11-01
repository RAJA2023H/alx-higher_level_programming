#!/usr/bin/python3
"""
empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    defines a rectangle
    """
    def __init__(self, widht=None, height=None):
        self.__widht = widht
        self.__height = height

    def width(self, value):
        try:
            self.__width = value
        except TypeError:
            print("width must be an integer")
        except ValueError:
            print("width must be >= 0")
    def width(self):
        return (self.__width)

    def height(self, value):
        try:
            self.__height = value
        except TypeError:
            print("height must be an integer")
        except ValueError:
             print("height must be >= 0")
    def height(self):
        return (self.__height)
