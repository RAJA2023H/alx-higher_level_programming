#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""


def add_integer(a, b=98):
    """
    function that adds 2 integers.
    a: first number
    b: second number

    Returns the addition of the two given numbers
    Raises TypeError if a or b aren't integer and/or float numbers

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
