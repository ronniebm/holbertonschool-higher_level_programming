#!/usr/bin/python3
"""
This module defines a City class to work
with the ORM MySQLAlchemy module.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class : links to the MySQL table cities.

    Attributes:
    ***********
    __tablename__ (str): --- table name of the class.
    id (int): -------------- id of the class.
    name (str): ------------ name of the class.
    state_id (int): -------- identifier number.

    ***********
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
