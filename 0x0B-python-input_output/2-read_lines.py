#!/usr/bin/python3
"""2-read_lines.py module"""


def read_lines(filename="", nb_lines=0):
    """
    read_lines: Read 'n' lines of a text file
    and prints it to stdoud.
    """

    counter = 0
    with open(filename, mode='r', encoding="utf-8") as fileObj:
        for lines in fileObj:
            print(lines, end="")
            counter += 1
            if counter == nb_lines:
                break
