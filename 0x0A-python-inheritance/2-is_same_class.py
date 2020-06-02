#!/usr/bin/python3
"""2-is_same_class.py module"""


def is_same_class(obj, a_class):
    """
    check if instance is of an specified class.

    Arguments:
    ----------
    obj {object} -- [datatype defined by the user]

    Returns:
    -------
    an specific message if TRUE, otherwise NOTHING.

    """
    return (type(obj) is a_class)
