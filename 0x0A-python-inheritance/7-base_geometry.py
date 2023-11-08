#!/usr/bin/python3
"""
currently empty class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """
        BaseGeometry class
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        checks if the value is ana int
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
