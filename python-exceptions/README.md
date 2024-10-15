# Python - Exceptions Project

This repository contains the solutions for the **Python Exceptions** project. The project focuses on error handling in Python, specifically how to use exceptions to manage and respond to errors in a controlled manner. By working through these tasks, you'll learn to write robust Python code that gracefully handles unexpected situations.

## 📝 Project Overview

In this project, you will explore how Python handles errors and exceptions. You'll learn the difference between errors and exceptions, how to raise exceptions, how to catch and handle them using `try`/`except`, and when to use `finally` for cleanup operations. The goal is to write resilient programs that can handle various types of runtime errors without crashing.

### Key Concepts:
- **Errors vs. Exceptions**: Understanding the difference between syntax errors and runtime exceptions in Python.
- **Handling Exceptions**: Using `try`, `except`, and `finally` blocks to catch and handle exceptions gracefully.
- **Raising Exceptions**: Learning how to raise built-in exceptions using `raise`.
- **Clean-up Actions**: Implementing clean-up code using `finally` to ensure that resources are properly released after an exception is handled.

### Skills Gained:
- Understanding how exceptions work in Python and how to handle them.
- Writing code that catches specific exceptions to handle different error cases.
- Raising exceptions with custom messages to alert users about specific conditions.
- Using `try`/`except` blocks to safely manage operations like division, list access, and printing.
- Implementing clean-up code using `finally` to ensure resources are released or tasks are completed.

## 📂 Project Structure

- **0-safe_print_list.py**: A function that prints `x` elements of a list and catches any exceptions that occur during printing.
- **1-safe_print_integer.py**: A function that prints an integer using `"{:d}".format()` and catches any exceptions if the value isn't an integer.
- **2-safe_print_list_integers.py**: A function that prints the first `x` integers in a list, skipping over non-integer elements.
- **3-safe_print_division.py**: A function that divides two integers, printing the result in the `finally` block, and returns the result or `None` if an exception occurs.
- **4-list_division.py**: A function that divides elements from two lists, handling division by zero, wrong types, and out-of-range errors.
- **5-raise_exception.py**: A function that raises a `TypeError` exception.
- **6-raise_exception_msg.py**: A function that raises a `NameError` exception with a custom message.
