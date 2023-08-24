#!/usr/bin/python3
"""
Module defines the class state & creates a declarative base instance.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# creates declarative base instance
Base = declarative_base()

# defines state class
class State(Base):
    """ State class definition """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
