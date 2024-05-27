#!/usr/bin/python3
"""reads a text file (UTF8)"""


def read_file(filename=""):
    """
        Reads and prints the content of a file line by line.
    """

    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
