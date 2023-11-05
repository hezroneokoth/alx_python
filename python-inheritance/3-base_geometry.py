#!/usr/bin/python3

"""This is a module that contains an empty class BaseGeometry."""
class BaseGeometry:
    """An empty class."""

    def __dir__(self):
        """Override dir() to exclude __init_subclass__."""
        return [attr for attr in dir(type(self)) if attr != '__init_subclass__']
