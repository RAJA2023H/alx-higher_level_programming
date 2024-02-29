#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    Args:
        - filename: JSON file
    """
    import json
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
