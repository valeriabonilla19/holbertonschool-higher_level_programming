#!/usr/bin/python3
"""
Module 5-save_to_json_file
Contains a function that writes an object to a text file
using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
