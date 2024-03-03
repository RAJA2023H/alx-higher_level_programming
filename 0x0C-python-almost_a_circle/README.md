This project aims to develop a Python package for managing geometric shapes such as rectangles and squares. The package includes classes for basic shape operations, including initialization, attribute validation, area calculation, display, and serialization/deserialization to JSON format.

Requirements:
All classes, methods, and attributes must be unit tested.
Code must adhere to PEP 8 style guidelines.
Serialization to JSON format is required for saving and loading shape instances from files.

## Project Structure

The project structure is organized as follows:

- **models**: This directory contains Python modules for different geometric shapes.
    - **base.py**: Contains the `Base` class, which serves as the base class for other shapes.
    - **rectangle.py**: Contains the `Rectangle` class, which represents rectangles.
    - **square.py**: Contains the `Square` class, which represents squares.

- **tests**: This directory contains unit tests for the classes implemented in the `models` directory.

## Features Implemented

- **Base Class**: The `Base` class serves as the base class for other shapes. It provides functionality for managing IDs of instances.

- **Rectangle Class**: The `Rectangle` class represents rectangles. It includes methods for calculating area, displaying the rectangle, and converting instances to dictionary representation.

- **Square Class**: The `Square` class inherits from the `Rectangle` class and represents squares. It includes methods for managing square-specific attributes.

- **Serialization**: Both `Rectangle` and `Square` classes include methods for serializing instances to JSON format and saving/loading instances from files.

- **Unit Testing**: All classes and methods are thoroughly unit tested to ensure reliability and correctness.

## Contributors

To run the unit tests for this project, navigate to the `tests` directory and execute the following command:

python3 -m unittest discover
