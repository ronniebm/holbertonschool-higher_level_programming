#!/usr/bin/python3
"""6-from_json_string.py module"""


import json


def from_json_string(my_str):
    """
    from_json_string: returns an object
    (Python data structure) represented
    by a JSON string:
    """
    return json.loads(my_str)
