# Python - Import & Modules Project

This repository contains the solutions for the **Python Import & Modules** project. The project focuses on how to import functions and variables from other Python files, create modules, and work with command-line arguments. You will learn how to reuse code by importing it into different scripts and make your programs dynamic by using command-line arguments.

## 📝 Project Overview

In this project, you will explore how Python modules work and how to import functions and variables from external files. You'll also learn how to handle command-line arguments to make your scripts dynamic and interactive. Additionally, you will learn how to prevent code from being executed when a script is imported as a module.

### Key Concepts:
- **Importing Functions and Variables**: Learn how to import specific functions and variables from other Python files.
- **Creating Modules**: Understand how to create reusable Python modules that can be imported into other scripts.
- **Using the `dir()` Function**: Discover how to list all names (functions, variables, etc.) defined in a module using the built-in `dir()` function.
- **Command-Line Arguments**: Use `sys.argv` to handle command-line arguments passed to a Python script.
- **Conditional Code Execution**: Learn how to prevent code in a Python script from being executed when the script is imported as a module.

### Skills Gained:
- Importing and using functions and variables from external files.
- Writing Python scripts that can handle command-line arguments dynamically.
- Understanding the concept of modules and how to use them to organize and reuse code.
- Using the `__name__ == "__main__"` construct to control the execution of scripts when imported.
- Printing names defined in modules using the `dir()` function.

## 📂 Project Structure

- **0-add.py**: Imports the function `add(a, b)` from `add_0.py` and prints the result of the addition of two integers.
- **1-calculation.py**: Imports functions from `calculator_1.py`, performs mathematical operations (addition, subtraction, multiplication, and division), and prints the results.
- **2-args.py**: Prints the number of arguments passed to the script and lists them.
- **3-infinite_add.py**: Adds all the command-line arguments passed to the script and prints the result.
- **4-hidden_discovery.py**: Prints all the names defined in the compiled `hidden_4.pyc` module, excluding names that start with `__`.
- **5-variable_load.py**: Imports the variable `a` from `variable_load_5.py` and prints its value.
