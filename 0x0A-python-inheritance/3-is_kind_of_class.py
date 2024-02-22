#!/usr/bin/python3
"""
function checks if an object is an instance of,
or if the object is an instance of a class that inherited from.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True or False
    Args: 
        obj: object
        a_class: class
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
