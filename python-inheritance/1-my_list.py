#!/usr/bin/python3
"""Module that defines the MyList class inheriting from list."""


class MyList(list):
    """A subclass of list with a method to print the list sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order (without modifying it)."""
        print(sorted(self))
