#!/usr/bin/python3
"""
Rectangle is a subclass that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Because we want to protect attributes of our class. With a setter,
    you are able to validate what a developer is trying to assign to
    a variable. So after, in your class you can “trust” these
    attributes.
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
        self.setter_validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.setter_validation("height", value, False)
        self.__height = value

    @property
    def x(self):
        """ x """
        return self.__x

    @x.setter
    def x(self, value):
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """ y """
        return self.__y

    @y.setter
    def y(self, value):
        self.setter_validation("y", value)
        self.__y = value

    def setter_validation(self, name, value, equal0=True):
        """
        validation of all setter methods and instantiation
        args:
            name, value, equal0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer". format(name))
        if equal0 and value < 0:
            raise ValueError("{} must be >= 0". format(name))
        if not equal0 and value <= 0:
            raise ValueError("{} must be > 0". format(name))

    def area(self):
        """
        returns the area value of the Rectangle instance
        """
        area = self.__width * self.__height
        return area

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for Y in range(self.__y):
            print("")
        for h in range(self.__height):
            for X in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ str method """
        Id = self.id
        x = self.__x
        y = self.__y
        return f"[Rectangle] ({Id}) {x}/{y} - {self.__width}/{self.__height}"

    def update(self, *args):
        """  assigns an argument to each attribute """
        num_args = len(args)
        if num_args > 0:
            self.id = args[0]
        if num_args > 1:
            self.__width = args[1]
        if num_args > 2:
            self.__height = args[2]
        if num_args > 3:
            self.__x = args[3]
        if num_args > 4:
            self.__y = args[4]
