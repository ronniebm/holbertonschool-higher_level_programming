#!/usr/bin/python3
"""2-read_lines.py module"""


def read_lines(filename="", nb_lines=0):
    """
    read_lines: Read 'n' lines of a text file
    and prints it to stdoud.
    """

    with open("./my_file_0.txt", mode='r', encoding='utf8') as fileObj:
        if nb_lines <= 0:
            print(fileObj.read(), end="")
        for i in range(nb_lines):
                print(fileObj.readline(), end="")
