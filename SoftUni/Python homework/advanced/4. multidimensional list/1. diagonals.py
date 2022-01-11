def read_matrix(count: int):
    matrix = []

    for current_row in range(count):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)

    return matrix


def primary_diagonal(matrix):
    primary_numbers = []
    primary_sum = 0

    for row in range(len(matrix)):
        current_number = matrix[row][row]
        primary_numbers.append(current_number)
        primary_sum += current_number

    return primary_numbers, primary_sum


def secondary_diagonal(matrix):
    secondary_numbers = []
    secondary_sum = 0
    size = len(matrix)

    for row in range(size):
        current_number = matrix[row][size - 1 - row]
        secondary_numbers.append(current_number)
        secondary_sum += current_number

    return secondary_numbers, secondary_sum


matrix = read_matrix(int(input()))
primary_diagonal_numbers, primary_sum = primary_diagonal(matrix)
secondary_diagonal_numbers, secondary_sum = secondary_diagonal(matrix)
print(f'Primary diagonal: {", ".join(map(str, primary_diagonal_numbers))}. Sum: {primary_sum}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal_numbers))}. Sum: {secondary_sum}')
