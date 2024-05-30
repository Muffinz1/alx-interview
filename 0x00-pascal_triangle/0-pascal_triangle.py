#!/usr/bin/python3
"""
Pascal triangle module
    - a triangle that has an arrangement of binomial coeffiecients
    - each number is the sum of two numbers above it
"""


def pascal_triangle(n):
    """
    Triangle function
        displays the Pascal's triangle according to n
    """
    if n <= 0:
        return []
    row_numbers = n
    triangle = [[1]]
    for i in range(row_numbers-1):
        temp = [0] + triangle[-1] + [0]
        row = []
        for j in range(len(triangle[-1]) + 1):
            row.append(temp[j] + temp[j+1])

        triangle.append(row)
    return triangle
