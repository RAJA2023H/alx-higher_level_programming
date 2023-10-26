#!/usr/bin/python3
"""
defining a class of Square with a private attribute
"""


class Square:
    """
    initializing a private attribute for instance of Square
    """
    def __init__(self, __size=0):
        """
        initialize size value
        """
        self.__size = __size

    @property
    def size(self):
        """
        return size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set new value of size
        """
        self.__size = value
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        returns the current square area
        """
        return self.__size*self.__size
