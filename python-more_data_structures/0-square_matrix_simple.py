#!/usr/bin/python3
"""
Module that defines a function to square all integers in a matrix.
"""


def square_matrix_simple(matrix=None):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix (list of lists of int): 2D list of integers.

    Returns:
        list of lists of int: New matrix with squared values.
    """
    if matrix is None:
        return []

    return [[element ** 2 for element in row] for row in matrix]
