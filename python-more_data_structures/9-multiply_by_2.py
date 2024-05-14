#!/usr/bin/python3
def best_score(a_dictionary):
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary
