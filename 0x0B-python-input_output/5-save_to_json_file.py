#!/usr/bin/python3
"""
This function writes the contents of a Python object (my_obj) to
a text file in JSON format. It serializes the Python object into
JSON and then writes it to the specified file.
"""


def save_to_json_file(my_obj, filename):
    """
    - my_obj: The Python object to be serialized and written to the file.
    
    - filename: The name of the file where the JSON data will be stored.
    If the file exists, its contents will be overwritten.

    - Return Value: The function does not return any value.
    It solely writes the JSON representation of the object to the specified file.
    """
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
