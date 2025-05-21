#!/usr/bin/python3
"""
Module that defines a function to square all integers in a matrix.
"""


from typing import List


def square_matrix_simple(matrix: List[List[int]] = None) -> List[List[int]]:
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix (List[List[int]]): 2D list of integers.

    Returns:
        List[List[int]]: New matrix with squared values.
    """
    if matrix is None:
        return []

    return [[element ** 2 for element in row] for row in matrix]
