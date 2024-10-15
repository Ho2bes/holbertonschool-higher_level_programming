# Python - Input/Output Project

This repository contains the solutions for the **Python Input/Output** project. The project focuses on reading from and writing to files in Python, working with JSON serialization and deserialization, and handling command-line arguments. You will learn how to manage file input/output operations and how to convert data structures between Python and JSON format.

## 📝 Project Overview

The project covers various aspects of file handling in Python, including opening, reading, writing, and appending to files. You will also explore JSON serialization and deserialization, which are key techniques for storing and exchanging data. By completing this project, you'll gain experience in working with files and JSON data, making your Python scripts more dynamic and interactive by accepting command-line arguments.

### Key Concepts:
- **File Handling**: Opening, reading, writing, and appending to files using Python's built-in functions and the `with` statement.
- **JSON Serialization**: Converting Python data structures (e.g., lists, dictionaries) into JSON strings.
- **JSON Deserialization**: Converting JSON strings back into Python data structures.
- **Command-Line Arguments**: Accessing and using command-line parameters in Python scripts.
- **Context Management**: Using the `with` statement to ensure that files are properly closed after being accessed.

### Skills Gained:
- How to open and close files in Python using the `with` statement.
- Reading file content in different ways, including reading the full file or line by line.
- Writing and appending to files in text mode.
- Converting Python data structures to JSON format and back.
- Working with command-line arguments using the `sys` module.

## 📂 Project Structure

- **0-read_file.py**: A function that reads a file and prints its content to stdout.
- **1-write_file.py**: A function that writes a string to a file and returns the number of characters written.
- **2-append_write.py**: A function that appends a string to the end of a file and returns the number of characters added.
- **3-to_json_string.py**: A function that returns the JSON representation of a Python object (string).
- **4-from_json_string.py**: A function that converts a JSON string into a Python data structure.
- **5-save_to_json_file.py**: A function that writes a Python object to a file using JSON representation.
- **6-load_from_json_file.py**: A function that creates a Python object from a JSON file.
- **7-add_item.py**: A script that adds all command-line arguments to a Python list and saves them to a file in JSON format.
- **8-class_to_json.py**: A function that returns a dictionary description for JSON serialization of an object.
- **9-student.py**: A `Student` class with public attributes for `first_name`, `last_name`, and `age`. Includes a method to retrieve a dictionary representation of the instance.
- **10-student.py**: Extends the `Student` class to allow filtering attributes to be included in the JSON dictionary representation.
- **11-student.py**: Further extends the `Student` class to allow loading attributes from a JSON object.
- **12-pascal_triangle.py**: A function that returns a list of lists representing Pascal's Triangle of size `n`.
