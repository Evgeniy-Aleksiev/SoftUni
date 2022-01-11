def read_matrix(count: int):
    matrix = []

    for current_row in range(count):
        row = [int(x) for x in input().split()]
        matrix.append(row)

    return matrix


def primary_diagonal(matrix):
    primary_sum = 0

    for row in range(len(matrix)):
        current_number = matrix[row][row]
        primary_sum += current_number

    return primary_sum


def secondary_diagonal(matrix):
    secondary_sum = 0
    size = len(matrix)

    for row in range(size):
        current_number = matrix[row][size - 1 - row]
        secondary_sum += current_number

    return secondary_sum


matrix = read_matrix(int(input()))
primary_diagonal_sum = primary_diagonal(matrix)
secondary_diagonal_sum = secondary_diagonal(matrix)
result = abs(primary_diagonal_sum - secondary_diagonal_sum)

print(result)
