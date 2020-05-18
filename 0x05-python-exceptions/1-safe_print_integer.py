#!/usr/bin/python3

"""
safe_print_integer: prints an integer with "{:d}".format().

@value: a value of any type (string, integer).
return: True if integer, else False.
"""


def safe_print_integer(value):

    try:
        print("{:d}".format(value))
        return(True)

    except ValueError:
        return(False)
