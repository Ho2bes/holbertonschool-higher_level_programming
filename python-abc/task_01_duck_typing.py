#!/usr/bin/env python3
"""create abstract class and his subclass"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    if isinstance(shape, Shape):
        print("Area:", shape.area())
        print("Perimeter:", shape.perimeter())
    else:
        print("Error: Object is not a valid shape.")
