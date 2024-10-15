# Python - Abstract Classes and Interfaces Project

This repository contains exercises designed to enhance your understanding and application of Object-Oriented Programming (OOP) concepts in Python, with a specific focus on **abstract classes**, **interfaces**, **duck typing**, and other advanced OOP principles.

## 📝 Project Overview

In this project, you'll dive deep into OOP concepts in Python, working with abstract base classes (ABC), interfaces, method overriding, and multiple inheritance. You'll also learn how to extend standard Python classes like lists and iterators. These exercises will help you master the design, implementation, and testing of Python programs using OOP principles.

### Key Concepts:
- **Abstract Classes**: Define abstract classes to establish common interfaces and ensure certain methods are implemented by subclasses.
- **Interfaces and Duck Typing**: Use interfaces and duck typing to ensure objects conform to specific contracts or protocols.
- **Subclassing Standard Classes**: Extend standard Python classes (e.g., lists, dictionaries) to create custom data structures with specialized behavior.
- **Method Overriding**: Modify or enhance base class methods to alter the behavior of subclasses.
- **Multiple Inheritance**: Explore complex class relationships by using multiple inheritance.
- **Mixins**: Compose behavior across unrelated classes using mixins.

### Skills Gained:
- Implementing abstract classes using Python's `ABC` module.
- Understanding and applying duck typing in Python to achieve flexibility in object behavior.
- Extending built-in Python classes like lists and iterators.
- Employing method overriding to refine and customize class behavior.
- Mastering multiple inheritance and understanding the method resolution order (MRO).
- Creating and using mixins to add functionality to multiple classes.

## 📂 Project Structure

- **task_00_abc.py**: Defines an abstract class `Animal` with an abstract method `sound`. Implements two subclasses `Dog` and `Cat` with their own `sound` methods.
- **task_01_duck_typing.py**: Creates a `Shape` abstract class and two concrete classes `Circle` and `Rectangle`. Demonstrates duck typing by creating a function `shape_info` to print the area and perimeter of any shape.
- **task_02_verboselist.py**: Extends the built-in `list` class to create a `VerboseList` class that prints a message when items are added or removed.
- **task_03_countediterator.py**: Implements a `CountedIterator` that tracks how many items have been iterated over by overriding the `__next__` method.
- **task_04_flyingfish.py**: Creates a `FlyingFish` class using multiple inheritance from `Fish` and `Bird`, overriding methods to explore method resolution order.
- **task_05_dragon.py**: Implements a `Dragon` class that inherits from `SwimMixin` and `FlyMixin`, demonstrating the power of mixins to add functionality across classes.
