def is_knight_placed(board, r, c):
    if 0 > r or 0 > c or len(board) <= r or len(board) <= c:
        return False
    return board[r][c] == 'K'


possible_moves = {
    'top_left_hor': lambda a, b: (a - 2, b - 1),
    'top_right_hor': lambda a, b: (a - 2, b + 1),
    'down_left_hor': lambda a, b: (a + 2, b - 1),
    'down_right_hor': lambda a, b: (a + 2, b + 1),
    'top_left_ver': lambda a, b: (a - 1, b - 2),
    'down_left_ver': lambda a, b: (a + 1, b - 2),
    'top_right_ver': lambda a, b: (a - 1, b + 2),
    'down_right_ver': lambda a, b: (a + 1, b + 2),
}

board_size = int(input())
matrix = []
total_removed_knight = 0

for _ in range(board_size):
    matrix.append(list(input()))

while True:
    max_count, knight_row, knight_col = 0, 0, 0
    for row in range(board_size):
        for col in range(board_size):
            if matrix[row][col] == '0':
                continue

            count = 0
            for move_index in possible_moves.values():
                new_row, new_col = move_index(row, col)
                if is_knight_placed(matrix, new_row, new_col):
                    count += 1

            if count > max_count:
                max_count, knight_row, knight_col = count, row, col
    if max_count == 0:
        break
    matrix[knight_row][knight_col] = '0'
    total_removed_knight += 1

print(total_removed_knight)