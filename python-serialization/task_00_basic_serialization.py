#!/usr/bin/env python3
"""basic serialization module that adds the functionality to serialize"""


import json


def serialize_and_save_to_file(data, filename):
  with open(filename, "w") as file:
        json.dump(data, file)
        pass

def load_and_deserialize(filename):
    with open("filename", "r") as file:
        filename = json.load(file)
        pass
