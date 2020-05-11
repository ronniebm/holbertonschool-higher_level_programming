#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if (a_dictionary is None):
        return (None)

    sort = sorted(a_dictionary.keys())

    for i in sort:
        print('{:s}: {}'.format(i, a_dictionary[i]))
