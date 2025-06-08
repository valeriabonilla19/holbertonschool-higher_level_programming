#!/usr/bin/python3
"""
Provides basic serialization and deserialization functions
for saving a dictionary to a JSON file and loading it back.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a dictionary and saves it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the output file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads data from a JSON file and deserializes it into a dictionary.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
