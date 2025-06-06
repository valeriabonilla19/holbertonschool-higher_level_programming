#!/usr/bin/python3
"""
Module 6-load_from_json_file
Contains a function that creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the file to load.

    Returns:
        The Python object represented by the JSON file content.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
