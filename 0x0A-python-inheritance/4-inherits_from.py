#!/usr/bin/python3
"""
Module check if an object is an instance
of a class that inherited from a specified class
"""


    def inherits_from(obj, a_class):
        """
        a function that returns True if the object is an instance
        of a class that inherited (directly or indirectly) from the
        specified class ; otherwise Falsei
        """

        return isinstance(type(obj), a_class) and not type(obj) != a_class
