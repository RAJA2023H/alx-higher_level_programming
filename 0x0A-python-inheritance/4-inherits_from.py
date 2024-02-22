#!/usr/bin/python3
"""
checks if the object is an instance of a class that 
inherited (directly or indirectly) from the specified class ;
"""


def inherits_from(obj, a_class):
    """
    Returns: True or False
    Args: 
    - obj : object
    - a_class : specified class
    """
    if isinstance(obj, a_class):
        if(type(obj) is not a_class):
            return True
    else:
        return False
