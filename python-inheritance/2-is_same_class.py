#!/usr/bin/python3
"""function that check if obj is class"""


def is_same_class(obj, a_class):
    """check if object is class"""
    if type(obj) is a_class:
        return True
    else:
        return False
