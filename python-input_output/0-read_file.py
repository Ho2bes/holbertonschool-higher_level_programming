#!/usr/bin/python3
"""function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        contenu = file.read()
        print(contenu)
