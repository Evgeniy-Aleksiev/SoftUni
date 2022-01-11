positions_to_check = {
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
    size_of_board = int(input())
    matrix = [[0] * size_of_board for n in range(size_of_board)]

    return matrix


def place_blombs(board):
    number_of_bombs = int(input())

    for _ in range(number_of_bombs):
        position = input()
        row, col = position[1:-1].split(', ')
        board[int(row)][int(col)] = '*'

    return board


def check_for_bombs(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            bombs_count = 0
            if board[row][col] == '*':
                continue
            for direction in positions_to_check:
                check_row = row + positions_to_check[direction][0]
                check_col = col + positions_to_check[direction][-1]
                if is_valid(len(board), check_row, check_col):
                    if board[check_row][check_col] == '*':
                        bombs_count += 1
            board[row][col] = bombs_count
    return board


board = get_board()
board_with_bombs = place_blombs(board)
for row in check_for_bombs(board_with_bombs):
    print(' '.join(map(str, row)))