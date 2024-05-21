#!/usr/bin/python3
"""A module that defines a class"""


class MyList(list):
    """Mylist: class that inherits from list
        Methods: print_sorted(self): sorts self
    """

    def print_sorted(self):
        """print list """
        print(sorted(self))
