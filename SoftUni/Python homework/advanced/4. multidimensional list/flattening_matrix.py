def read_matrix():
    matrix = []
    rows_count = int(input())

    for current_row in range(rows_count):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)

    flattened = []

    for row in matrix:
        for el in row:
            flattened.append(el)

    return flattened


def print_result(result):
    print(result)


matrix = read_matrix()
print_result(matrix)

