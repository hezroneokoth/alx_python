#!/usr/bin/python3
""" A Rectangle module with the class Rectangle"""
from models.base import Base

class Rectangle(Base):
    """ Rectangle class that inherits from Base """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method that initializes the objects shown """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """ This method calculates and returns the area of the Rectangle"""
        return self.__width * self.__height
    
    def display(self):
        """ This method displays the Rectangle -- taking care of x and y -- with # characters"""
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
            
    def __str__(self):
        """ This method overrides __str__ to return [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """ This method adds arguments to attributes in the given order"""
        attributes = ["id", "width", "height", "x", "y"]
        for index, value in enumerate(args):
            setattr(self, attributes[index], value)
