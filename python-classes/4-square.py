#!/usr/bin/python3
"""contain class Square."""


class Square:
    """Class of a square."""

    def __init__(self, size=0):
        """Initialize a square with option size"""
        self.size = size

    @property
    def size(self):
        """get a size of square"""
        return self._size

    @size.setter
    def size(self, value):
        """Define size of square with check"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Calculate and return the area of square."""
        return self._size ** 2
