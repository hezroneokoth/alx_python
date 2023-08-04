#!/usr/bin/python3

"""This is a module that contains an empty class BaseGeometry."""
class BaseGeometry:
    """An empty class."""

    def __dir__(self):
        """Override dir() to exclude __init_subclass__."""
        attributes = super().__dir__()
        attributes.remove('__init_subclass__')
        return attributes


bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))
