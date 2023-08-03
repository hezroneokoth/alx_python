#!/usr/bin/python3

"""This is a module that contains a class BaseGeometry."""

class BaseGeometry:
    """This is an empty class BaseGeometry."""

    def __init__(self):
        """An __innit__ method that initializes the attribute self."""
        pass

    def __dir__(self):
        """A custom __dir__ method to override default behavior."""
        return []
    
bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))