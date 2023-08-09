#!/usr/bin/python3
""" A square module with the class Square"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """ A Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor method that initializes the objects size, x, y, and id"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ This method overrides the  __str__ method and returns [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
