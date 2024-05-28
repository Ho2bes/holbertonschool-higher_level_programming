#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file."""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_arguments_to_list(filename, *args):
    try:
        existing_list = load_from_json_file(filename)
    except FileNotFoundError:
        existing_list = []

    new_list = existing_list + list(args)
    save_to_json_file(new_list, filename)


if __name__ == "__main__":
    filename = "add_item.json"
    arguments = sys.argv[1:]
    add_arguments_to_list(filename, *arguments)
