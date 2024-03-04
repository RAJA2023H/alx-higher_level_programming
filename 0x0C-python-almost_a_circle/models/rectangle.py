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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def get_width(self):
        return self.__width

    @width.setter
    def set_width(self, value):
        self.__width = value
    
    @property
    def get_height(self):
        return self.__height

    @height.Setter
    def set_height(self, value):
        self.__height = value

    @property
    def get_x(self):
        return self.__x

    @x.Setter
    def set_x(self, value):
        self.__height = value

    @property
    def get_y(self):
        return self.__y

    @y.Setter
    def set_y(self, value):
        self.__y = value
