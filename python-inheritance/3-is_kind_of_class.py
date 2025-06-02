#!/usr/bin/python3
"""
Function that checks if an object is an instance of a class,
or a class that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or inherits from a_class"""
    return isinstance(obj, a_class)
