#!/usr/bin/python3

"""This is a module that contains a class BaseGeometry with an area() function."""

class BaseGeometry:
    """This is a class containing area() method."""
    
    def area(self):
        """This method raises an exception that area() is not implemented."""
        raise Exception("area() is not implemented")

""" excludes the __init_subclass__"""
attributes = [attr for attr in dir(BaseGeometry) if attr != '__init_subclass__']

print(attributes)