#!/usr/bin/python3
"""
define a class of Square with a private attribute
"""


class Square:
    """
    initializing a private attribute for instance of Square
    """
    def __init__(self, __size=0, position=(0, 0)):
        """
        initialize size value
        """
        self.__size = __size
        self.__position = position

    @property
    def size(self):
        """
        getter method
        return size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method
        set new value of size
        """
        self.__size = value
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """
        getter method
        return size value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter method
        set new value of position
        """
        self.__position = value
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        returns the current square area
        """
        return self.__size*self.__size

    def my_print(self):
        """
        prints in stdout the square
        """
        if self.__size <= 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for y in range(self.__size):
                print(" "*self.__position[0], end='')
                print("#"*self.__size)
