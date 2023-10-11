#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
           v = i ** 2
           new_row.append(v)
        new_matrix.append(new_row)
    return new_matrix
