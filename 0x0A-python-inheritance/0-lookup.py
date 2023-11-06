#!/usr/bin/python3
"""
lists all available
attributes and methods of an object
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    Args:
        obj: object

    """

    return dir(obj)
