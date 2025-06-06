#!/usr/bin/python3
"""
Module 0-read_file
Contains a function that reads a text file and prints its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.
                        Defaults to an empty string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
