#!/usr/bin/python3

"""This is a module that contains a function inherits_from."""


def inherits_from(obj, a_class):
    """
    This method/function checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
