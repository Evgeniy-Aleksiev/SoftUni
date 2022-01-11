def read_matrix(count: int):
    matrix = []

    for current_row in range(count):
        matrix.append(list(input()))

    return matrix


def find_the_first_occurrence(matrix):
    symbol = input()
    position = None
    size = len(matrix)

    for row in range(size):
        for col in range(size):
            if symbol == matrix[row][col]:
                position = (row, col)
                break
        if position:
            break

    return position, symbol


matrix = read_matrix(int(input()))
current_position, symbol = find_the_first_occurrence(matrix)
print(current_position if current_position else f'{symbol} does not occur in the matrix')