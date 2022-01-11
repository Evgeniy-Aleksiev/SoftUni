def read_matrix(is_test):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0]
        ]
    rows_count, columns_count = map(int, input().split(', '))
    matrix = []

    for row in range(rows_count):
        matrix.append(list(map(int, input().split(', '))))

    for row in matrix:
        print(row)
        for col in row:
            print(col)

    return matrix


is_test = False
print(read_matrix(is_test))
print(len(read_matrix(is_test)))
