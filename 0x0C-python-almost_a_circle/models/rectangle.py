#!/usr/bin/python3
"""
Rectangle is a subclass that inherits from Base
"""
from  models.base import Base


class Rectangle(Base):
    """
    Because we want to protect attributes of our class. With a setter,
    you are able to validate what a developer is trying to assign to a variable.
    So after, in your class you can “trust” these attributes.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
    
    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """ x """
        return self.__x

    @x.setter
    def x(self, value):
        self.__height = value

    @property
    def y(self):
        """ y """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value