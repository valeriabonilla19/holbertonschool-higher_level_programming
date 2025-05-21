#!/usr/bin/python3
"""
Module that defines a function to find the key with the biggest integer value.
"""


def best_score(a_dictionary):
    """
    Returns the key with the highest integer value in the dictionary.

    Args:
        a_dictionary (dict): A dictionary with integer values.

    Returns:
        str: Key with the highest value, or None if dictionary is empty or None.
    """
    if not a_dictionary:
        return None

    max_key = None
    max_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key
