# Helpers for getting matrix options from a tuple
ROWS = 0
COLUMNS = 1
MATRIX = 2

# Menu choices
ADD_MATRICES = '1'
MULTIPLY_MATRIX_BY_CONSTANT = '2'
MULTIPLY_MATRICES = '3'
TRANSPOSE_MATRIX = '4'
EXIT = '0'


def read_matrix_size(msg):
    rows_count, columns_count = (int(n) for n in input(msg).split())
    return rows_count, columns_count


def read_row():
    return [float(n) for n in input().split()]


def read_matrix(size_msg, matrix_msg):
    rows_count, columns_count = read_matrix_size(size_msg)
    print(matrix_msg)
    matrix = []
    for _ in range(rows_count):
        matrix.append(read_row())
    return rows_count, columns_count, matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


def read_constant(msg):
    return float(input(msg))


def print_menu():
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate determinant
6. Inverse matrix
0. Exit""")


def get_user_menu_choice():
    return input("Your choice: ")


def print_cannot_perform():
    print("The operation cannot be performed.")


def print_result(matrix):
    print("The result is:")
    print_matrix(matrix)


def add_matrices():
    matrix_a = read_matrix('Enter size of first matrix: ', 'Enter first matrix:')
    matrix_b = read_matrix('Enter size of second matrix: ', 'Enter second matrix: ')

    if matrix_a[ROWS] != matrix_b[ROWS] or matrix_a[COLUMNS] != matrix_b[COLUMNS]:
        print_cannot_perform()
    else:
        a_plus_b = [list(map(sum, zip(*t))) for t in zip(matrix_a[MATRIX], matrix_b[MATRIX])]
        print_result(a_plus_b)


def multiply_matrix_by_constant():
    matrix_a = read_matrix('Enter size of matrix: ', 'Enter matrix: ')
    constant = read_constant('Enter constant: ')

    product = [[constant * x for x in row] for row in matrix_a[MATRIX]]
    print_result(product)


def multiply_matrices():
    matrix_a = read_matrix('Enter size of first matrix: ', 'Enter first matrix:')
    matrix_b = read_matrix('Enter size of second matrix: ', 'Enter second matrix: ')

    if matrix_a[COLUMNS] == matrix_b[ROWS]:
        product = [[sum(a * b for a, b in zip(row_a, col_b))
                    for col_b in zip(*matrix_b[MATRIX])] for row_a in matrix_a[MATRIX]]
        print_result(product)
    else:
        print_cannot_perform()


def make_zero_matrix(rows, columns):
    matrix = []
    while len(matrix) < rows:
        matrix.append([])
        while len(matrix[-1]) < columns:  # -1 index is the last array (row) that’s been appended to the array.
            matrix[-1].append(0.0)
    return matrix


def transpose_along_main_diagonal():
    matrix = read_matrix('Enter matrix size: ', 'Enter matrix: ')
    matrix_transposed = make_zero_matrix(matrix[ROWS], matrix[COLUMNS])
    for i in range(matrix[ROWS]):
        for j in range(matrix[COLUMNS]):
            matrix_transposed[j][i] = matrix[MATRIX][i][j]
    print_result(matrix_transposed)


def transpose_along_side_diagonal():
    matrix = read_matrix('Enter matrix size: ', 'Enter matrix: ')
    matrix_transposed = make_zero_matrix(matrix[ROWS], matrix[COLUMNS])
    for i in range(matrix[ROWS]):
        for j in range(matrix[COLUMNS]):
            matrix_transposed[i][j] = matrix[MATRIX][-j-1][-i-1]
    print_result(matrix_transposed)


def transpose_along_vertical_line():
    matrix = read_matrix('Enter matrix size: ', 'Enter matrix: ')
    matrix_transposed = make_zero_matrix(matrix[ROWS], matrix[COLUMNS])
    for i in range(matrix[ROWS]):
        matrix_transposed[i] = reversed(matrix[MATRIX][i])
    print_result(matrix_transposed)


def transpose_along_horizontal_line():
    matrix = read_matrix('Enter matrix size: ', 'Enter matrix: ')
    matrix_transposed = make_zero_matrix(matrix[ROWS], matrix[COLUMNS])
    for i in range(matrix[ROWS]):
        matrix_transposed[i] = matrix[MATRIX][-i-1]
    print_result(matrix_transposed)


def transpose_matrix():
    main_diagonal = '1'
    side_diagonal = '2'
    vertical_line = '3'
    horizontal_line = '4'

    print()
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")

    inp = input("Your choice: ")
    if inp == main_diagonal:
        transpose_along_main_diagonal()
    if inp == side_diagonal:
        transpose_along_side_diagonal()
    if inp == vertical_line:
        transpose_along_vertical_line()
    if inp == horizontal_line:
        transpose_along_horizontal_line()


while True:
    print_menu()
    choice = get_user_menu_choice()
    if choice == EXIT:
        break
    elif choice == ADD_MATRICES:
        add_matrices()
    elif choice == MULTIPLY_MATRIX_BY_CONSTANT:
        multiply_matrix_by_constant()
    elif choice == MULTIPLY_MATRICES:
        multiply_matrices()
    elif choice == TRANSPOSE_MATRIX:
        transpose_matrix()
