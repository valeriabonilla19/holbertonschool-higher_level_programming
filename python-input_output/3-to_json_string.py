#!/usr/bin/python3
"""
Module 3-to_json_string
Contains a function that returns the JSON representation of an object (string).
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object as a string.

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
