def read_matrix(is_test):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0]
        ]

    row_count, columns_count = map(int, input().split(', '))
    matrix = []

    for current_row in range(row_count):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


def matrix_sum(matrix):
    total_sum = 0
    for row in matrix:
        for col in row:
            total_sum += col
    return total_sum


def output(matrix):
    print(matrix_sum(matrix))
    print(matrix)


is_test = False
matrix_elements = read_matrix(is_test)
matrix_sum(matrix_elements)
output(matrix_elements)
