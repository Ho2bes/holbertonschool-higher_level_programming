#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    "create a student class"
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        "return a dictionnary"
        dico = {}
        if hasattr(self, "__dict__"):
            dico = self.__dict__.copy()
        return dico
