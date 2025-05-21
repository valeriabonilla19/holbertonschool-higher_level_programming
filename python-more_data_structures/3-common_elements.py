#!/usr/bin/python3
"""
Module that defines a function to return common elements in two sets.
"""


def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    Args:
        set_1 (set): First set.
        set_2 (set): Second set.

    Returns:
        set: A set containing common elements.
    """
    return set_1 & set_2
