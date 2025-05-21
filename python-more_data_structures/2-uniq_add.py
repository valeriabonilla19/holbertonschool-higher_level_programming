#!/usr/bin/python3
"""
Module that defines a function to add all unique integers in a list.
"""


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.

    Args:
        my_list (list): The list of integers.

    Returns:
        int: The sum of unique integers.
    """
    return sum(set(my_list))
