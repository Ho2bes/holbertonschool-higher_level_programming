#!/usr/bin/python3
"""function that writes an Object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """use JSON representation"""
    my_obj_json = json.dumps(my_obj)
    with open(filename, 'w') as file:
        file.write(my_obj_json)
