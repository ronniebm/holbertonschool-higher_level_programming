#!/usr/bin/python3
"""9-add_item.py script"""

from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = \
    __import__('8-load_from_json_file').load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except:
    items = []

items.extend(argv[1:])
save_to_json_file(items, "add_item.json")
