#!/usr/bin/python3
"""8-load_from_json_file.py module"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file: creates an
    Object from a "JSON file"

    Arguments:
    ---------
    filename [str] -- name of the file.

    Returns:
    --------
    object: a JSON object
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.loads(file.read())
