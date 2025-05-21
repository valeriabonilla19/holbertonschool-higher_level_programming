#!/usr/bin/python3
"""
Module that defines a function to return elements only present in one set.
"""


def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one of the two sets.

    Args:
        set_1 (set): First set.
        set_2 (set): Second set.

    Returns:
        set: A set with elements in either set_1 or set_2 but not both.
    """
    return set_1 ^ set_2
