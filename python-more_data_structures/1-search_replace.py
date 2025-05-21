#!/usr/bin/python3
"""
Module that defines a function to replace occurrences
of an element in a list with another element.
"""


def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of 'search' with 'replace' in a new list.

    Args:
        my_list (list): The original list.
        search: The element to replace.
        replace: The new element to replace with.

    Returns:
        list: A new list with replaced values.
    """
    return [replace if item == search else item for item in my_list]
