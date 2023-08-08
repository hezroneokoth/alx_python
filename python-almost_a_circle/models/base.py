#!/usr/bin/python3
""" A Base module containing the class Base."""

class Base:
    """ The Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """An initialization contructor/method"""
        
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
