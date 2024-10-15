# Python - More Classes and Objects Project

This repository contains the solutions for the **Python - More Classes and Objects** project. The project builds upon the basics of object-oriented programming (OOP) by introducing more advanced concepts such as class attributes, static methods, and overriding special methods (`__str__`, `__repr__`). By working through these tasks, you will learn how to manipulate and design more complex classes in Python.

## 📝 Project Overview

This project deepens your understanding of Object-Oriented Programming (OOP) in Python. You will work with **class attributes**, **instance attributes**, **special methods** (`__str__`, `__repr__`), and **methods like `staticmethod` and `classmethod`**. You will also implement concepts such as comparing objects, managing class-level data, and handling object creation dynamically.

### Key Concepts:
- **Classes and Instances**: Understanding the difference between class attributes and instance attributes.
- **Special Methods**: How to define and override `__str__`, `__repr__`, and other built-in methods to control object behavior.
- **Class Methods and Static Methods**: Understanding when and how to use `@classmethod` and `@staticmethod`.
- **Properties**: Using getter and setter methods to control access to private attributes.
- **Object Deletion**: Handling instance deletion and tracking class-level data with class attributes.
- **Comparing Objects**: Implementing methods to compare objects based on their attributes.
- **Creating new instances dynamically**: Using class methods to define new instances with specific parameters.

### Skills Gained:
- Creating classes with instance and class attributes.
- Using and overriding special methods such as `__str__`, `__repr__`, and `__del__`.
- Implementing class and static methods to add functionality at the class level.
- Using getter and setter properties to validate and manage attribute access.
- Tracking the number of instances created and deleted.
- Comparing objects and creating new instances with class methods.

## 📂 Project Structure

- **0-rectangle.py**: Defines an empty `Rectangle` class.
- **1-rectangle.py**: Adds `width` and `height` private instance attributes, along with getter and setter methods for each, with type and value validation.
- **2-rectangle.py**: Adds methods to calculate the `area()` and `perimeter()` of the rectangle.
- **3-rectangle.py**: Overrides the `__str__` method to print the rectangle using the `#` character.
- **4-rectangle.py**: Overrides the `__repr__` method to return a string that can recreate the rectangle instance using `eval()`.
- **5-rectangle.py**: Adds a `__del__` method that prints "Bye rectangle..." when an instance is deleted.
- **6-rectangle.py**: Adds a public class attribute `number_of_instances` to track how many instances of `Rectangle` are created and deleted.
- **7-rectangle.py**: Adds a public class attribute `print_symbol` to define the symbol used for the string representation of the rectangle.
- **8-rectangle.py**: Adds a static method `bigger_or_equal` that compares the area of two rectangles and returns the larger one.
- **9-rectangle.py**: Adds a class method `square` that returns a new `Rectangle` instance where width and height are equal.
