#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix, row_sqr = [], []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            row_sqr.append(matrix[i][j] * matrix[i][j])
        new_matrix.append(row_sqr)
        row_sqr = []
    return new_matrix
