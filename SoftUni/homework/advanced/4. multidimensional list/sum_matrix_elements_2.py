def read_matrix():
    matrix = []
    total_sum = 0

    row_count, column_count = [int(x) for x in input().split(', ')]

    for current_row in range(row_count):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
        total_sum += sum(row)

    return matrix, total_sum


def print_result(matrix, matrix_sum):
    print(matrix_sum)
    print(matrix)


matrix, result = read_matrix()
print_result(matrix, result)
