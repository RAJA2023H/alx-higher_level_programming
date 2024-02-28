#!/usr/bin/python3
"""
function that returns the JSON
representation of an object(string)
"""


def to_json_string(my_obj):
    """
    returns the JSON serialised representation of an object
    Args:
        - my_obj : the object tha we want to serialize
    """
    import json
    return (json.dumps(my_obj))
