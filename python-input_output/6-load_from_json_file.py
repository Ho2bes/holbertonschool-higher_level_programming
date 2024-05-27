#!/usr/bin/python3
"""a function that creates an Object from a “JSON file”"""

def load_from_json_file(filename):
    """ a function that creates an Object from a “JSON file”"""
    with open(filename, "r") as file:
        obj_json = json.load(file)
        return obj_json
