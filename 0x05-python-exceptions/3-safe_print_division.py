#!/usr/bin/python3

"""
safe_print_division(a, b): divides 2 integers and prints the result.

@a: first number.
@b: second number.
return: result of operation.
"""


def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
