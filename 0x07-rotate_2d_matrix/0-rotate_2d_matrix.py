#!/usr/bin/python3
"""
Rotating A 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Defining a function to rotate the 2d matrix
    """
    # flipping the matrix mathmatically
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # reversing rows
    for row in matrix:
        row.reverse()