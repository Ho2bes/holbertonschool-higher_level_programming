#!/usr/bin/env python3
"""basic serialization module that adds the functionality to serialize"""


import json


def serialize_and_save_to_file(data, filename):
    """Serialize data and save it to a file."""
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize data from a file."""
    with open(filename, "r") as file:
        return json.load(file)
