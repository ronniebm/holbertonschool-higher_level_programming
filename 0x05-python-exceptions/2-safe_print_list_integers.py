#!/usr/bin/python3

"""
safe_print_list_integers: prints first x elements of a list & only integers.

@value: a value of any type (string, integer).
return: True if integer, else False.
"""


def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    for i in range(0, x):
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                counter += 1
        except (TypeError):
            break
    print()
    return counter
