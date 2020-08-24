# Write a program that reads a matrix and a constant and outputs the result of their multiplication.
# The first line of the input contains the number of rows and the number of columns of the matrix. 
# Next lines contain rows of the matrix. The last line contains the constant.
# The constant and the elements of the matrix are integers.

def read_rows_columns_count():
    return (int(n) for n in input().split())


def read_row():
    return [int(n) for n in input().split()]


def read_matrix():
    matrix = []
    rows_count, columns_count = read_rows_columns_count()
    for _ in range(rows_count):
        matrix.append(read_row())
    return rows_count, columns_count, matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


def read_constant():
    return int(input())


ROWS = 0
COLUMNS = 1
MATRIX = 2


matrix_a = read_matrix()
constant = read_constant()

product_constant_matrix = [[constant * x for x in row] for row in matrix_a[MATRIX]]
print_matrix(product_constant_matrix)
