#!/usr/bin/python3
"""14-pascal_triangle.py module"""

def pascal_triangle(n):
    """
    pascal_triangle: returns a list of
    lists of integers representing the
    Pascal’s triangle of 'n' int.

    Arguments:
    ----------
    n [int] -- a given number.

    Returns:
    --------
    a 'list' of lists.
    """

    """checking condition"""
    if n <= 0:
        return []

    pascal = []
    row = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(i):
                row.append(sum(pascal[-1][j:j+2]))
        pascal.append(row)
    return (pascal)
