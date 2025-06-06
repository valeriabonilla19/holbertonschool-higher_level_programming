#!/usr/bin/python3
"""
Module 4-from_json_string
Contains a function that returns a Python object from a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON string to a corresponding Python object.

    Args:
        my_str (str): The JSON string.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
