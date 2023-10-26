#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """
    initializing a private attribute for instance of Square
    """
    def __init__(self, size=0):
        """
        initialize size value
        """
        self.size = size

    def area(self):
        """
        returns the current square area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set new value of position
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """
        prints in stdout the square
        """
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__size):
                print("".join(["#" for j in range(self.__size)]))
