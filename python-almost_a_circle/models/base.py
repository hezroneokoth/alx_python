#!/usr/bin/python3
""" A base module containing the class base."""

class base:
    """The base class."""
    __nb_objects = 0

    def __innit__ (self, id=None):
        """An initialization contructor/method"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
