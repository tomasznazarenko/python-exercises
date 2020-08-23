# Write a program that:
# 
#     Reads matrix A from the input.
#     Reads matrix B from the input.
#     Outputs their sum if it is possible to add them. Otherwise, it should output the ERROR message.
# 
# Each matrix in the input is given in the following way: the first line contains the number of rows n and the number of columns m. 
# Then n lines follow, each containing mintegers representing one row of the matrix.
# 
# Output the result in the same way but don't print the dimensions of the matrix.
#
# Example 1:
# 
# Input:
# 
# 4 5
# 1 2 3 4 5
# 3 2 3 2 1
# 8 0 9 9 1
# 1 3 4 5 6
# 4 5
# 1 1 4 4 5
# 4 4 5 7 8
# 1 2 3 9 8
# 1 0 0 0 1
# 
# Output:
# 
# 2 3 7 8 10
# 7 6 8 9 9
# 9 2 12 18 9
# 2 3 4 5 7
# 
# Example 2:
# 
# Input:
# 
# 2 3
# 1 4 5
# 4 5 5
# 4 5
# 0 1 0 4 5
# 1 7 8 9 4
# 1 2 3 5 6
# 1 3 4 3 8
# 
# Output:
# 
# ERROR

def read_rows_columns():
    return (int(n) for n in input().split())


def read_row():
    return [int(n) for n in input().split()]


def read_matrix():
    matrix = []
    rows_count, columns_count = read_rows_columns()
    for _ in range(rows_count):
        matrix.append(read_row())
    return rows_count, columns_count, matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


ROWS_M = 0
COLUMNS_N = 1
MATRIX = 2

matrix_a = read_matrix()
matrix_b = read_matrix()

if matrix_a[ROWS_M] != matrix_b[ROWS_M] or matrix_a[COLUMNS_N] != matrix_b[COLUMNS_N]:
    print("ERROR")
else:
    a_plus_b = [list(map(sum, zip(*t))) for t in zip(matrix_a[MATRIX], matrix_b[MATRIX])]
    print_matrix(a_plus_b)
