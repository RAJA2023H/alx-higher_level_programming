#!/usr/bin/python3
"""
 function that checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Returns: True or False
    Args:
        obj: object
        a_class: class
    """

    if type(obj) is a_class:
        return (True)
    else:
        return(False)
