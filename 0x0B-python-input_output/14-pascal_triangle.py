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
        return ([])

    pascal = [[1]]
    last = pascal[0]
    for row in range(n - 1):
        new = [1]
        for col in range(row + 1):
            if col >= row:
                new.append(1)
            else:
                val = last[col] + last[col + 1]
                new.append(val)
        pascal.append(new)
        last = new
    return (pascal)
