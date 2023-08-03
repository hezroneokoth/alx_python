#!/usr/bin/python3

class Square:
    """This is a class that defines a square."""
    
    def __init__(self, size=0):
        """This method/constructor initializes the Square instance with an optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
