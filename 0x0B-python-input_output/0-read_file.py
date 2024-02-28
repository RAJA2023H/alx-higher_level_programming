#!/usr/bin/python3
"""
This function reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Read and prints the file content to stdout
    Arg: filename
    """
    # open and reads the file:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        # prints the file content
        print(content)
