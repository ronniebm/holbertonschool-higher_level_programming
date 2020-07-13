#!/usr/bin/python3
"""5-to_json_string.py module"""


import json


def to_json_string(my_obj):
    """
    to_json_string: returns the JSON
    representation of an object (string).
    """
    print (my_obj)
    return json.dumps(my_obj)
