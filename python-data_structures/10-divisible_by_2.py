#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copied_list = my_list.copy()
    for element in copied_list:
        if element % 2 == 0:
            return True
        else:
            return False
