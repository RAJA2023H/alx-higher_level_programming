#!/usr/bin/python3
"""
Module check if an object is an instance
of a class that inherited from a specified class
"""


def inherits_from(obj, a_class):
    """
    function that check if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class

        
    """

    return isinstance(type(obj), a_class) and not type(obj) != a_class
