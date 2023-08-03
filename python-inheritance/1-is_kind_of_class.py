#!/usr/bin/python3

"""This is a module that contains a function is_kind_of_class"""

def is_kind_of_class(obj, a_class):
    """
    This method/function checks if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; False otherwise.
    """
    return type(obj) is a_class
