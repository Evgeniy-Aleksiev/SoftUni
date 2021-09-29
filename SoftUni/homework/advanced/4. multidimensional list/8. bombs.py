def is_valid(matrix, r, c, bomb):

    # top left diagonal
    if 0 <= r - 1 < len(matrix) and 0 <= c - 1 < len(matrix):
        if matrix[r - 1][c - 1] > 0:
            matrix[r - 1][c - 1] -= bomb

    # top
    if 0 <= r - 1 < len(matrix) and 0 <= c < len(matrix):
        if matrix[r - 1][c] > 0:
            matrix[r - 1][c] -= bomb

    # top right diagonal
    if 0 <= r - 1 < len(matrix) and 0 <= c + 1 < len(matrix):
        if matrix[r - 1][c + 1] > 0:
            matrix[r - 1][c + 1] -= bomb

    # right
    if 0 <= r < len(matrix) and 0 <= c - 1 < len(matrix):
        if matrix[r][c - 1] > 0:
            matrix[r][c - 1] -= bomb

    # left
    if 0 <= r < len(matrix) and 0 <= c + 1 < len(matrix):
        if matrix[r][c + 1] > 0:
            matrix[r][c + 1] -= bomb

    # left down diagonal
    if 0 <= r + 1 < len(matrix) and 0 <= c - 1 < len(matrix):
        if matrix[r + 1][c - 1] > 0:
            matrix[r + 1][c - 1] -= bomb

    # down
    if 0 <= r + 1 < len(matrix) and 0 <= c < len(matrix):
        if matrix[r + 1][c] > 0:
            matrix[r + 1][c] -= bomb

    # right down diagonal
    if 0 <= r + 1 < len(matrix) and 0 <= c + 1 < len(matrix):
        if matrix[r + 1][c + 1] > 0:
            matrix[r + 1][c + 1] -= bomb

    return matrix


matrix = []

matrix_size = int(input())
alive_cells = 0
alice_cells_sum = 0

for row in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

bomb_coordinates = input().split()

for x in bomb_coordinates:
    coord_r, coord_c = [int(n) for n in x.split(',')]
    current_coordinate = matrix[coord_r][coord_c]

    if current_coordinate > 0:
        matrix[coord_r][coord_c] = 0
        matrix = is_valid(matrix, coord_r, coord_c, current_coordinate)

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            alice_cells_sum += el

print(f'Alive cells: {alive_cells}')
print(f'Sum: {alice_cells_sum}')

for el in matrix:
    print(' '.join(str(x) for x in el))
