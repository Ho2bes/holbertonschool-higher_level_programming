#!/usr/bin/env python3
"""deserialize custom Python objects using the pickle module"""


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return None
        except Exception as e:
            print("Error:", e)
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print(f"Error: File '{filename}' no CustomObject instance")
                    return None
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return None
        except pickle.UnpicklingError:
            print(f"Error: File '{filename}' is not a valid pickle file.")
            return None
        except Exception as e:
            print("Error:", e)
            return None
