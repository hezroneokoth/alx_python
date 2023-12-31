#!/usr/bin/python3

"""
This module is for a class square

that defines a square by a private instance attribute 'size'.
"""

class Square:
    """This is a class that defines a square."""

    def __init__(self, size=0):
        """This method/constructor initialize the Square instance with an optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        """This second method/constructor calculates and returns the area of the square."""
        return self.__size ** 2
