#!/usr/bin/python3

"""
safe_print_division(a, b): divides 2 integers and prints the result.

@a: first number.
@b: second number.
return: result of operation.
"""


def safe_print_division(a, b):
    counter = 0

    for i in range(0, x):
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                counter += 1
        except TypeError:
            break
    print()
    return counter
