#!/usr/bin/python3

"""
This module is for a class square

that defines a square by a private instance attribute 'size'.
"""

class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """This method initialize the Square instance with an optional size."""
        self.size = size
    
    @property
    def size(self):
        """This getter method retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """This setter method sets the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
        """This method calculates and returns the area of the square."""
        return self.__size ** 2
    
    def my_print(self):
        """This method prints the square with # characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
