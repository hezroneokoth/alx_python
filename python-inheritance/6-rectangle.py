#!/usr/bin/python3

"""This is a module that contains a Rectangle class that inherits from BaseGeometry"""

class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """This __innit__ method Initialize a Rectangle instance with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
