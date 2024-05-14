#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_element = my_list[0]
    for element in my_list:
        if element > max_element:
            max_element = element
            return max_element
