#!/usr/bin/python3

class Square:
    """This is a class that defines a square.
    
    It has one method that contains two attributes i.e. self and size.
    """
    
    def __init__(self, size):
        """This method/constructor initializes the Square instance with a given size.
        
        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The size of the square.
        """
        self.__size = size
