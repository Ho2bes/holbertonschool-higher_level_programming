#!/usr/bin/python3
"""a function that returns an object represented by a JSON"""


import json


def from_json_string(my_str):
    """return an object"""
    return json.loads(my_str)
