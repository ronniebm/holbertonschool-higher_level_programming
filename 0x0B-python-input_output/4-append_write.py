#!/usr/bin/python3
"""4-append_write.py module"""


def append_write(filename="", text=""):
    """
    append_write: appends a string at the
    end of a text file (UTF8) and returns
    the number of characters added.

    Arguments:
    ---------
    filename [str] -- file to be created.
    text [str] -- text to be written.

    Returns:
    --------
    value [int] -- number of appended characters.
    """

    with open(filename, mode='a', encoding='utf8') as fileObj:
        return(fileObj.write(text))
