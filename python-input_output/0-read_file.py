#!/usr/bin/python3
"""function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    with open('filename=""', 'r') as fichier:
        contenu = fichier.read()
        print(contenu)
