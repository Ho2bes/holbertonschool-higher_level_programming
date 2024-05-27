#!/usr/bin/python3
"""a function returns the dictionary description with simple data structure"""


import json


def class_to_json(obj):
    """function returns dictionary"""
    dico = {}
    if hasattr(obj, "__dict__")
        dico = obj.__dict__.copy()

    return dico

