#!/usr/bin/python3
"""1-number_of_lines.py module"""


def number_of_lines(filename=""):
    """
    number_of_lines: Todo.
    """
    counter = 0
    with open("./my_file_0.txt", mode='r', encoding='utf8') as fileObj:
        for line in fileObj:
            counter += 1
        return (counter)
