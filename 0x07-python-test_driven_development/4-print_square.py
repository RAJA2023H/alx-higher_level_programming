#!/usr/bin/python3
"""
Module that import a function that  prints a square with the character #
"""


def print_square(size):
    """
    function that prints a square with the character #
    size is the size length of the square


    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
