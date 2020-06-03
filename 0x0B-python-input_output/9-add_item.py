#!/usr/bin/python3
"""9-add_item.py script"""

from sys import argv
from os import path

if __name__ == "__main__":
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file
    filename = 'add_item.json'

    if path.isfile(filename):
        new_list = load_from_json_file(filename)
    else:
        new_list = []

    for i in range(1, len(argv)):
        new_list.append(argv[i])

    save_to_json_file(new_list, filename)
