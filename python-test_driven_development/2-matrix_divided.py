#!/usr/bin/python3
"""Divide all elements of a matrix"""

def matrix_divided(matrix, div):

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or \
            any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) \
                                 of integers/floats")

            new_row.append(round(value / div, 2))
        new_matrix.append(new_row)

    return new_matrix
