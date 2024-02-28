Python - Input/Output


Certainly, here's another version of the README:

Python Input/Output Project
Author: Guillaume
Weight: 1
Duration: Feb 6, 2024, 4:00 AM - Feb 7, 2024, 4:00 AM

Project Overview
This Python project focuses on input and output operations, particularly file handling and JSON serialization/deserialization. The tasks are designed to strengthen understanding of core Python concepts and best practices.

Learning Objectives
Upon completion of this project, you should be able to:

Understand the importance of Python programming.
Perform various file operations including reading, writing, and appending.
Manipulate file cursors and ensure proper file closure.
Utilize the with statement for efficient file handling.
Grasp the concepts of JSON, serialization, and deserialization.
Convert Python data structures to JSON strings and vice versa.
Resources
Official Python Documentation: Reading and Writing Files
Python Context Managers and the with Statement
Dive Into Python 3: Chapter 11 - Files
JSON Encoder and Decoder in Python
File Operations in Python - Programiz
Automate the Boring Stuff with Python (Ch. 8 & 14)
Python File Handling - GeeksforGeeks
Requirements
Python Scripts
Editors: Use vi, vim, or emacs.
Interpretation/Compilation: The scripts must run on Ubuntu 20.04 LTS using Python 3.8.5.
File Endings: Ensure all files end with a new line.
Shebang Line: Begin all files with #!/usr/bin/python3.
README: Include a README.md file at the root of the project folder.
Code Style: Adhere to PEP 8 guidelines (pycodestyle version 2.8.*).
Executable Files: All files should be executable.
File Length: Be mindful of file length; use wc to test.
Documentation: Provide documentation for all modules, classes, and functions.
Python Test Cases
File Endings: Test files should end with a new line.
Test Folder: Place test files inside a folder named tests.
Execution: Execute all tests using python3 -m doctest ./tests/*.
Tasks
Read File

Function: def read_file(filename=""):
Action: Read a text file (UTF8) and print its contents to stdout.
Write to File

Function: def write_file(filename="", text=""):
Action: Write a string to a text file (UTF8) and return the number of characters written.
Append to File

Function: def append_write(filename="", text=""):
Action: Append a string to the end of a text file (UTF8) and return the number of characters added.
To JSON String

Function: def to_json_string(my_obj):
Action: Return the JSON representation of an object (string).
From JSON String to Object

Function: def from_json_string(my_str):
Action: Return an object (Python data structure) represented by a JSON string.
Save Object to File

Function: def save_to_json_file(my_obj, filename):
Action: Write an object to a text file using a JSON representation.
Create Object from JSON File

Function: def load_from_json_file(filename):
Action: Create an object from a JSON file.
Class to JSON

Function: def class_to_json(obj):
Action: Return the dictionary description for JSON serialization of a class object.
Student to JSON

Class: Student
Attributes: first_name, last_name, age
Method: to_json() returns a dictionary representation of a Student instance.
Student to JSON with Filter

Enhancement: Optional attribute filtering for Task 9.
Student to Disk and Reload

Enhancement: Serialization and deserialization using file handling.
Pascal's Triangle

Function: def pascal_triangle(n):
Action: Return a list of lists of integers representing Pascal’s triangle of n.
GitHub Repository
Repository: alx-higher_level_programming
Directory: 0x0B-python-input_output
