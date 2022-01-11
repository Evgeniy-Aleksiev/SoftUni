def read_matrix():
    matrix = []
    count = int(input())

    for row in range(count):
        current_row = [int(x) for x in input().split()]
        matrix.append(current_row)
    return matrix


def get_sum_primary_diagonal(matrix):
    size = len(matrix[0])
    total_sum = 0

    for row in range(size):
        total_sum += matrix[row][row]

    return total_sum


def get_sum_below_diagonal(matrix):
    size = len(matrix[0])
    total_sum = 0
    for row in range(size):
        for col in range(size):
            if row >= col:
                total_sum += matrix[row][col]

    return total_sum


def get_sum_top_of_diagonal(matrix):
    size = len(matrix[0])
    total_sum = 0
    for row in range(size):
        for col in range(size):
            if row <= col:
                total_sum += matrix[row][col]

    return total_sum


def reversed_diagonal(matrix):
    diagonal_sum = 0
    size = len(matrix[0])

    for row in range(size):
        diagonal_sum += matrix[row][size - row - 1]

    return diagonal_sum


matrix = read_matrix()
print(get_sum_primary_diagonal(matrix))
print(get_sum_below_diagonal(matrix))
print(get_sum_top_of_diagonal(matrix))
print(reversed_diagonal(matrix))