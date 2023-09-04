#!/usr/bin/python3

"""matrix division"""


def matrix_divided(matrix, div):

    "divide matrix by division"""
    new_matrix = []

    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    if len(matrix) == 0:
        raise TypeError(msg1)

    size = len(matrix[0])

    for row in matrix:
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError(msg1)

        if len(row) != size:
            raise TypeError(msg2)

        if div == 0:
            raise ZeroDivisionError("division by zero")

        new_matrix.append([round(i/div, 2) for i in row])

    return new_matrix
