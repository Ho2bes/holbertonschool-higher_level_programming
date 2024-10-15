# Python - Inheritance Project

This repository contains solutions for the **Python Inheritance** project. The project explores the concept of inheritance in object-oriented programming (OOP) and how it is implemented in Python. By working through these tasks, you will learn how to inherit properties and methods from base classes, override methods, and create complex class hierarchies.

## 📝 Project Overview

Inheritance is a core concept in object-oriented programming that allows a class to inherit attributes and methods from another class. This project focuses on understanding the use of inheritance in Python, exploring how to create subclasses, and how to use built-in functions like `super()`, `isinstance()`, and `issubclass()`. You will also learn how to define multiple base classes, override methods, and validate data in a class.

### Key Concepts:
- **Inheritance**: The mechanism by which one class can inherit attributes and methods from another class.
- **Superclass (Base Class)**: A class whose properties and methods are inherited by another class.
- **Subclass**: A class that inherits properties and methods from a superclass.
- **Overriding Methods**: A subclass can override methods from the superclass to provide specific functionality.
- **Multiple Inheritance**: A class can inherit from multiple base classes in Python.
- **Built-in Functions**: Use of `isinstance()`, `issubclass()`, `type()`, and `super()` to work with inheritance.

### Skills Gained:
- Creating subclasses that inherit from base classes.
- Overriding methods in subclasses to customize behavior.
- Using `super()` to call methods from a superclass.
- Validating attributes and raising exceptions in class methods.
- Working with Python’s `isinstance()` and `issubclass()` functions to check types and inheritance relationships.

## 📂 Project Structure

- **0-lookup.py**: A function that returns the list of available attributes and methods of an object.
- **1-my_list.py**: A class `MyList` that inherits from `list` and implements a method `print_sorted()` to print the list in ascending order.
- **2-is_same_class.py**: A function that checks if an object is exactly an instance of a specified class.
- **3-is_kind_of_class.py**: A function that checks if an object is an instance of a class or a class that inherited from the specified class.
- **4-inherits_from.py**: A function that checks if an object is an instance of a class that inherited from a specified class.
- **5-base_geometry.py**: An empty class `BaseGeometry`.
- **6-base_geometry.py**: Extends `BaseGeometry` by adding a public instance method `area()` that raises an exception with the message "area() is not implemented".
- **7-base_geometry.py**: Adds a public instance method `integer_validator(self, name, value)` to validate integers in `BaseGeometry`.
- **8-rectangle.py**: A class `Rectangle` that inherits from `BaseGeometry`, with instantiation of width and height.
- **9-rectangle.py**: Extends the `Rectangle` class by implementing the `area()` method and customizing `__str__()` to print the rectangle’s dimensions.
- **10-square.py**: A class `Square` that inherits from `Rectangle` and implements instantiation with size.
- **11-square.py**: Extends the `Square` class by customizing `__str__()` to print the square’s description.
