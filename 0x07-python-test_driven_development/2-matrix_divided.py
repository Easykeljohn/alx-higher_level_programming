#!usr/bin/python3

"""defines function to scalar divide matrix"""

def matrix_division(matrix, div):
    """divides matrix by scalar integer rounded to two decimal places"""
    import decimal
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_msg)
    lenRows = []
    rowCount = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        lenRows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_msg)
        rowCount += 1
    if len(set(lenRows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
                        list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
