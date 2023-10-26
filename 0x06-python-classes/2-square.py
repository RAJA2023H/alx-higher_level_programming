#!/usr/bin/python3
"""
class Square that defines a square
"""


class Square:
    """
    initializing a private attribute for instance
    """
    def __init__(self, size=0):
        """
        checking if __size is integer
        checking if __size is less than zero
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
