def read_matrix():
    matrix = []
    row_count, columns_count = [int(x) for x in input().split(', ')]

    for current_row in range(row_count):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)

    return matrix


def get_sum_of_matrix(matrix, row_index, col_index, size):
    the_sum = 0

    for r in range(row_index, row_index + size):
        for c in range(col_index, col_index + size):
            the_sum += matrix[r][c]
    return the_sum


def get_best_matrix_sum(matrix, matrix_size):
    best_row_index = 0
    best_col_index = 0
    best_sum = get_sum_of_matrix(matrix, 0, 0, matrix_size)

    for r in range(len(matrix) - matrix_size +1):
        for c in range(len(matrix[r]) - matrix_size +1):
            current_sum = get_sum_of_matrix(matrix, r, c, matrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = r
                best_col_index = c

    return best_row_index, best_col_index


def print_result(indexes, size):
    (row_index, col_index) = indexes
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))
    print(get_sum_of_matrix(matrix, row_index, col_index, size))


matrix_size = 2
matrix = read_matrix()
coordinates = get_best_matrix_sum(matrix, matrix_size)
print_result(coordinates, matrix_size)
