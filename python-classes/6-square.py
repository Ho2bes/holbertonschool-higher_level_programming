#!/usr/bin/python3
"""contain class Square."""


class Square:
    """Class of a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with option size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get a size of square"""
        return self._size

     @position.setter
    def position(self, value):
        """Définit place of the square with check."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

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

    def my_print(self):
        """print a stdout square with #"""
        if self._size == 0:
            print("")
            return
        for _ in range(self._position[1]):
            print("")
        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)
