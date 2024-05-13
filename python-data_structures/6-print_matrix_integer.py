#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_row = ' '.join(map(str, row))
        print("{}".format(formatted_row))
