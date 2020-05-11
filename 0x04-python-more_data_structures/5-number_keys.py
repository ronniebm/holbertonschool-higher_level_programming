#!/usr/bin/python3
def number_keys(a_dictionary):
    if (a_dictionary is None):
        return (None)

    keys = 0

    for i in a_dictionary:
        keys += 1
    return (keys)
