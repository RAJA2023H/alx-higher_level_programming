#!/usr/bin/python3
"""
Module check if an object is an instance
of a class that inherited from a specified class
"""


def inherits_from(obj, a_class):
    """
    Function that check if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class

    Returns True if(inherits) False (otherwise)
    
    """

    return isinstance(obj, a_class) and not type(obj) is a_class
