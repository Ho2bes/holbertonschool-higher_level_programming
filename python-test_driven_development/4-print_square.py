#!/usr/bin/python3
"""print a square with the character '#' """

def print_square(size):
    """
    print a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")
