#!/usr/bin/python3
"""
Module that defines a function to delete a key in a dictionary.
"""


def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to delete.

    Returns:
        dict: The updated dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
