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

    def update(self, *args, **kwargs):
        """ updates the Square methode update"""
        if args:
            l = len(args)
            if l > 0:
                self.id = args[0]
            if l > 1:
                self.size = args[1]
            if l > 2:
                self.x = args[2]
            if l > 3:
                self.y = args[3]
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
