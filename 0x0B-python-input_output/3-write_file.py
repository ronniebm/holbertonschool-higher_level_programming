#!/usr/bin/python3
"""3-write_file.py module"""


def write_file(filename="", text=""):
    """
    write_file: writes a string to a text file (UTF8)
    and returns the number of characters written.

    Arguments:
    ---------
    filename [str] -- file to be created.
    text [str] -- text to be written.

    Returns:
    --------
    value [int] -- number of characters wroted.
    """

    with open(filename, mode='w+', encoding='utf8') as fileObj:
        return(fileObj.write(text))
