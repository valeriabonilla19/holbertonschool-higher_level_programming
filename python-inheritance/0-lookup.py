#!/usr/bin/python3
"""Module that defines the `lookup` function."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
