#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    the class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        returns string infor about the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """ property getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value
