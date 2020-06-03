#!/usr/bin/python3
"""0-read_file.py module"""


def read_file(filename=""):
    """
    read_file: reads the given file.
    """
    with open("./my_file_0.txt", mode='r', encoding='utf8') as fileObj:
        for line in fileObj:
            print(line, end="")
