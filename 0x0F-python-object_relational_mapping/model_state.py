#!/usr/bin/python3
"""
A module that contains the class definition of a State
and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# creating an instance.
Base = declarative_base()


# State class, that inherits from Base.
class State(Base):
    """A class representation of a State."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
