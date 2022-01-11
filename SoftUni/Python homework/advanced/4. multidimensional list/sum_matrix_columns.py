def read_matrix():
    matrix = []
    rows_count, columns_count = map(int, input().split(', '))

    for current_col in range(rows_count):
        row = [int(x) for x in input().split()]
        matrix.append(row)

    return matrix, columns_count


def columns_sum(matrix, columns_count):
    col_sum = []
    row_count = len(matrix)

    for column in range(columns_count):
        column_sum = 0
        for row in range(row_count):
            column_sum += matrix[row][column]
        col_sum.append(column_sum)

    return col_sum


def print_result(result):
    for el in result:
        print(el)


matrix, col_count = read_matrix()
list_of_sum = columns_sum(matrix, col_count)
print_result(list_of_sum)
