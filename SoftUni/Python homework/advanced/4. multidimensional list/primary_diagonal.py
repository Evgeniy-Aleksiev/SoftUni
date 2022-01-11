def read_matrix(n):
    matrix = []

    for row in range(n):
        current_row = [int(x) for x in input().split()]
        matrix.append(current_row)

    return matrix


def primary_diagonal(matrix):
    diagonal_sum = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if col == row:
                diagonal_sum += matrix[row][col]

    return diagonal_sum


matrix = read_matrix(int(input()))
print(primary_diagonal(matrix))


