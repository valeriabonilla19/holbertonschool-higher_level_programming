#!/usr/bin/python3
"""
Function that returns the dictionary description
with simple data structure (list, dict, str, int, bool)
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of obj for JSON serialization.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: Dictionary containing serializable attributes of obj.
    """
    return obj.__dict__.copy()
