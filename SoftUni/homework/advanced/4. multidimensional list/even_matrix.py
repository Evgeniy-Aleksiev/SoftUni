def read_matrix():
    matrix = []
    row_count = int(input())

    for current_row in range(row_count):
        row = [int(x) for x in input().split(', ')]
        matrix.append([])
        for el in row:
            if el % 2 == 0:
                matrix[current_row].append(el)
    return matrix


def result_print(result):
    print(result)


matrix = read_matrix()
result_print(matrix)
