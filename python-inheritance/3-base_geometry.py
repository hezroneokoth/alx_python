#!/usr/bin/python3

"""This is a module that contains an empty class BaseGeometry."""

class BaseGeometry:
    """This is an empty class BaseGeometry."""

    def __dir__(self):
        """This __dir__ method overrides the behaviour of dir() to exclude __init_subclass__"""
        attributes = list(super().__dir__())
        attributes.remove('__init_subclass__')
        return attributes
