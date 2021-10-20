directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'right': [0, 1],
    'left': [0, -1],
    'up_left': [-1, -1],
    'up_right': [-1, 1],
    'down_left': [1, -1],
    'down_right': [1, 1]
}


def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_board():
    matrix = []
    king_row, king_col = 0, 0

    for row in range(8):
        current_row = input().split()
        matrix.append(current_row)
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'K':
                king_row, king_col = row, col

    return matrix, king_row, king_col


def is_king_safe(board, row, col):
    checked_row, checked_col = row, col
    queen_coordinates = []

    # check up position
    for direction in directions:
        while True:
            next_row = checked_row + directions[direction][0]
            next_col = checked_col + directions[direction][1]

            if not is_valid(len(board), next_row, next_col):
                break

            if board[next_row][next_col] == 'Q':
                queen_coordinates.append([next_row, next_col])
                break

            checked_row, checked_col = next_row, next_col
        checked_row, checked_col = row, col

    return queen_coordinates


board, king_r, king_c = get_board()
coordinates = is_king_safe(board, king_r, king_c)

if coordinates:
    [print(cord) for cord in coordinates]
else:
    print("The king is safe!")