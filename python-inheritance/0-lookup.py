#!/usr/bin/python3
"""Returns a list of methods"""


def lookup(obj):
    """lists methods in obj"""
    list = dir(obj)
    return list
