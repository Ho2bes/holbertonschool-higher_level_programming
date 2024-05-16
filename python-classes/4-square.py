#!/usr/bin/python3
"""contain python code"""


class Square:
    """contain a simple class of square"""

    def __init__(self, size=0):
        """Initialize a square with option size"""
        self.__size = size

    def area(self):
        """calculate the area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """get a size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """define size of square with check"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
