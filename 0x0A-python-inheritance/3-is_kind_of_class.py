#!/usr/bin/python3
"""3-is_kind_of_class.py module"""


def is_kind_of_class(obj, a_class):
    """Function that checks of object is instance of, or if
    is instance of class that inherited from, the specified
    class; otherwise FALSE.

    Arguments:
    ----------
    obj {object} -- [datatype defined by the user].
    a_class {class} -- [classtype given by the user].

    Returns: True if is instance, otherwise False.
    ----------
    """
    return (isinstance(obj, a_class))
