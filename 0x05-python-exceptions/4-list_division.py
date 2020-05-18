#!/usr/bin/python3

"""
list_division: divides element by element 2 lists.

@my_list1: a list that can contain any type.
@my_list2: a list that can contain any type.
return: a new list with all divisions.
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)

    return (new_list)
