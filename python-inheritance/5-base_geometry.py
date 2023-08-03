#!/usr/bin/python3

"""This is a module that contains a class BaseGeometry with an area() function."""

class BaseGeometry:
    """A class with area and integer validation methods."""

    def area(self):
        """A Method to calculate the area (not implemented in this base class)."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate and handle integer values."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
