#!/usr/bin/python3
"""
check if same object
"""


def is_same_class(obj, a_class):
    """
    check if the obj is an instance of the specified class
    obj: object
    a_class: class
    returns True if the object is exactly an instance of
    the specified class ;otherwise False
    """

    if obj.__class__ is a_class:
        return True
    else:
        return False
