#!/usr/bin/python3
"""7-save_to_json_file.py module"""


import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file: writes an Object to a
    text file, using a JSON representation.

    Arguments:
    ---------
     my_obj [object] -- Object.
     filename [str] -- name of the file.
    """
    with open(filename, mode='w', encoding='utf-8') as fileObj:
        fileObj.write(json.dumps(my_obj))
