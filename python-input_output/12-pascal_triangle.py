#!/usr/bin/python3
"""Module that defines a function to generate Pascal's triangle"""


def pascal_triangle(n):
    """Generate Pascal's triangle of n rows

    Args:
        n: number of rows in the triangle

    Returns:
        List of lists representing Pascal's triangle
        Empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Create a new row
        row = []

        for j in range(i + 1):
            # First and last elements are always 1
            if j == 0 or j == i:
                row.append(1)
            else:
                # Sum of two elements from previous row
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        triangle.append(row)

    return triangle
