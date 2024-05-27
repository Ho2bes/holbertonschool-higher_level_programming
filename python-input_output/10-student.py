#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    "create a student class"
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        "return a dictionnary"
        if attrs is None:
            return self.__dict__

        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)

        return json_dict

    def reload_from_json(self, json):
        """replace attribute info"""
        if not json:
            return
        self.age = json["age"]
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]

