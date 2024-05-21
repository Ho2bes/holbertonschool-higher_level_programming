#!/usr/bin/python3
"""class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inherit of BaseGeometry"""

    def __init__(self, width, height):
        self.__height = height
        self.__width = width
        self.integer_validator("height", height)
        self.integer_validator("width", width)

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
