# 0x0A. Python - Inheritance

Python OOP project covering inheritance concepts.

## Description

This project focuses on understanding and implementing inheritance in Python. It covers various topics including superclass, subclass, method overriding, class hierarchy, and more.

## Learning Objectives

- Understand the concept of inheritance in Python.
- Learn to define classes and create class hierarchies.
- Understand the use of super() function.
- Implement method overriding and inheritance.
- Learn about multiple inheritance.
- Gain proficiency in using isinstance(), issubclass(), and other built-in functions related to inheritance.

## Files

The project consists of the following Python scripts:

1. **0-lookup.py**: A function that returns the list of available attributes and methods of an object.
2. **1-my_list.py**: A class `MyList` that inherits from `list` and provides a method to print the list sorted.
3. **2-is_same_class.py**: A function to check if an object is exactly an instance of a specified class.
4. **3-is_kind_of_class.py**: A function to check if an object is an instance of, or inherited from, a specified class.
5. **4-inherits_from.py**: A function to check if an object is an instance of a class that inherited from a specified class.
6. **5-base_geometry.py**: An empty class `BaseGeometry`.
7. **6-base_geometry.py**: A class `BaseGeometry` with a method `area()` that raises an exception.
8. **7-base_geometry.py**: A class `BaseGeometry` with a method `integer_validator()` for integer validation.
9. **8-rectangle.py**: A class `Rectangle` that inherits from `BaseGeometry` with private width and height attributes.
10. **9-rectangle.py**: A class `Rectangle` with implemented `area()` method and custom string representation.
11. **10-square.py**: A class `Square` that inherits from `Rectangle` with a square-specific constructor and area calculation.
12. **11-square.py**: A class `Square` with a custom string representation for squares.

## Testing

Test cases for each script are provided in the `tests` directory. They can be executed using the `doctest` module as follows:

```bash
python3 -m doctest ./tests/*

