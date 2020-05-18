#!/usr/bin/python3

"""
safe_print_integer_err: prints an integer.

@value: a value of any type (string, integer).
return: True if integer, else False and prints stderr msg.
"""


def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return(True)

    except (TypeError, ValueError) as error:
        from sys import stderr
        print("Exception: {}".format(error), file=stderr)
        return(False)
