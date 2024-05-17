#!/usr/bin/python3
"""containing the Square class."""


class Square:
    """Class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with an optional size."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square with checks."""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        """Set the position of the square with checks."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("Position must be a tuple of 2 non-negative integers")
        self._position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self._size ** 2

    def my_print(self):
        """Print the square."""
        if self._size == 0:
            print("")
            return
        for _ in range(self._position[1]):
            print("")
        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)
