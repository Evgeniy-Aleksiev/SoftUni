def read_matrix():
    matrix = []
    rows_count = int(input())

    for i in range(rows_count):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    evens = [[x for x in row if x % 2 == 0] for row in matrix]

    return evens


def print_result(result):
    print(result)


matrix = read_matrix()
print_result(matrix)