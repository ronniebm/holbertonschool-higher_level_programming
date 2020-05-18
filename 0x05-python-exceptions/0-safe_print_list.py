#!/usr/bin/python3

"""
safe_print_list: prints x elements of a list.
@my_list: a list holding any type.
@x: number of elements to print.
return: number of elements printed.
"""


def safe_print_list(my_list=[], x=0):
    counter = 0

    for i in range(0, x):
        try:
            print(my_list[i], end="")
            counter += 1
        except IndexError:
            break
    print()
    return counter
