#!/usr/bin/python3
"""Definition of to json function """


import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
