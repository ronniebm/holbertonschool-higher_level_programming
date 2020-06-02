#!/usr/bin/python3
"""4-inherits_from.py module"""


def inherits_from(obj, a_class):
    """Function that recturns True if the object is
    instance of a class that inherited (directly or
    indirectly) from the specified class; otherwise
    FALSE.

    Arguments:
    ----------
    obj {object} -- [datatype defined by the user].
    a_class {class} -- [classtype given by the user].

    Returns: True if is instance, otherwise False.
    ----------
    TRUE if direct/indirect instance, otherwise FALSE.
    """
    if type(obj) is a_class:
        return (False)
    return issubclass(type(obj), a_class)
