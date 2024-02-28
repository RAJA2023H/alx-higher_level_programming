#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    write to a file and return the number of charscters written
    Args:
        - filenamw: name of the file
        - text: the content that we want to write
    """
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(text))
