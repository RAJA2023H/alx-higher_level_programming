#!/usr/bin/python3
"""
Module composed by a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.

    Args:
        matrix: list of lists of integers or floats
        div: a number

    Returns a new matrix


    """
    msg_err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(msg_err)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    divlist = []

    if len(matrix) == 0:
        return matrix
    ref_len = len(matrix[0])
    for row in matrix:
        if len(row) != ref_len:
            raise TypeError(msg_err)
        divrow = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(msg_err)
            x = i / div
            divrow.append(round(x, 2))
        divlist.append(divrow)

    return divlist


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
