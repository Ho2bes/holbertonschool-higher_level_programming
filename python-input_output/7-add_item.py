#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file."""


import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_items_to_list():
    """Add all command line arguments to a Python list and save to a file."""
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, "add_item.json")
