#!/usr/bin/python3

"""
This is a module that contains a function is_same_class

It checks if the object is an exact instance of the specified class.
"""

def is_same_class(obj, a_class):
    """
    This method/function shecks if the object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class; False otherwise.
    """
    return type(obj) is a_class
