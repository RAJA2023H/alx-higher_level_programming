#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    divlist = []
    if len(matrix) < 2 :
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    ref_len = len(matrix[0])
    for row in matrix:
        if len(row) != ref_len:
            raise TypeError("Each row of the matrix must have the same size")
        divrow = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            x = i / div
            divrow.append(round(x, 2))
        divlist.append(divrow)
    return divlist
