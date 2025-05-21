#!/usr/bin/python3
"""
Module that defines a function to return a new dictionary
with all values multiplied by 2.
"""


def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The original dictionary with integer values.

    Returns:
        dict: A new dictionary with values doubled.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
