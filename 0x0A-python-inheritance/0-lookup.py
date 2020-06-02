#!/usr/bin/python3
"""Defining a new class"""


def lookup(obj):
    """
     This function returns a list of attributes and
     methods of a given object.

     Arguments:
     ----------
       obj {object} -- [a given object]
    """
    return dir(obj)
