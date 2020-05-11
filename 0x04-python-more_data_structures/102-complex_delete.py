#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    find = []
    for i, j in a_dictionary.items():
        if value == j:
            find.append(i)

    for key in find:
        del a_dictionary[key]
    return a_dictionary
