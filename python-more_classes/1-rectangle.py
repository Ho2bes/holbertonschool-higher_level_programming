#!/usr/bin/python3
"""contain python code"""


class Rectangle:
    """contain a simple class of rectangle"""

def __init__(self, width=0, height=0):
    self._width = width
    self._height = height

@property
def width(self):
    return self._width

@width.setter
def width(self, value):
    if width is not int:
        raise TypeError ("width must be an integer")
    if width < 0:
        raise ValueError ("width must be >= 0")

@property
def height(self):
    return self._height

@height.setter
def height(self, value):
    if height is not int:
        raise TypeError ("height must be an integer")
    if height < 0:
        raise ValueError ("height must be >= 0")
