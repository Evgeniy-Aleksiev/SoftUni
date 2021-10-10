def is_valid_player_choice(choice, board):
    is_column_index_valid = 0 <= choice < len(board[0])
    has_column_space = is_column_index_valid and board[0][choice] is None
    return is_column_index_valid and has_column_space


def player_choice(player):
    choice = input(f'Player {player}, please choose a column\n')
    return int(choice) - 1


def applying_current_choice(player_index, choice_index, board):
    row_index = 0
    while row_index < len(board) and board[row_index][choice_index] is None:
        row_index += 1

    board[row_index - 1][choice_index] = player_index
    return row_index - 1, choice_index


def get_right_win_condition_values(board, row, col, max_col_index):
    right_win_condition = [board[row][c] for c in range(col, max_col_index)]
    return right_win_condition


def get_left_win_condition_values(board, row, col, min_col_index):
    left_win_condition = [board[row][c] for c in range(col, min_col_index, -1)]
    return left_win_condition


def get_up_win_condition_values(board, row, col, min_row_index):
    up_win_condition = [board[r][col] for r in range(row, min_row_index, -1)]
    return up_win_condition


def get_down_win_condition_values(board, row, col, max_row_index):
    down_win_condition = [board[r][col] for r in range(row, max_row_index)]
    return down_win_condition


def get_left_up_win_condition_values(board, row, col, min_col, min_row):
    values = []
    max_diagonal = min(
        abs(min_row - row),
        abs(min_col - col)
    )

    for diagonal in range(max_diagonal):
        r = row - diagonal
        c = col - diagonal
        values.append(board[r][c])

    return values


def get_right_up_win_condition_values(board, row, col, max_col, min_row):
    values = []
    max_diagonal = min(
        abs(min_row - row),
        max_col - col
    )
    for diagonal in range(max_diagonal):
        r = row - diagonal
        c = col + diagonal
        values.append(board[r][c])

    return values


def get_left_down_condition_values(board, row, col, min_col, max_row):
    values = []
    max_diagonal = min(
        max_row - row,
        abs(min_col - col)
    )
    for diagonal in range(max_diagonal):
        r = row + diagonal
        c = col - diagonal
        values.append(board[r][c])

    return values


def get_right_down_win_condition_values(board, row, col, max_col, max_row):
    values = []
    max_diagonal = min(
        max_row - row,
        max_col - col
    )
    for diagonal in range(max_diagonal):
        r = row + diagonal
        c = col + diagonal
        values.append(board[r][c])

    return values


def check_for_win(board, row_index, col_index, win_count):
    min_column_index = max(col_index - win_count, -1)
    max_column_index = min(col_index + win_count, len(board[row_index]))

    min_row_index = max(row_index - win_count, -1)
    max_row_index = min(row_index + win_count, len(board))

    right_win_condition_values = get_right_win_condition_values(
        board,
        row_index,
        col_index,
        max_column_index
    )

    left_win_condition_values = get_left_win_condition_values(
        board,
        row_index,
        col_index,
        min_column_index
    )

    up_win_condition_values = get_up_win_condition_values(
        board,
        row_index,
        col_index,
        min_row_index
    )

    down_win_condition_values = get_down_win_condition_values(
        board,
        row_index,
        col_index,
        max_row_index
    )

    left_up_win_condition_values = get_left_up_win_condition_values(
        board,
        row_index,
        col_index,
        min_column_index,
        min_row_index
    )

    right_up_win_condition_values = get_right_up_win_condition_values(
        board,
        row_index,
        col_index,
        max_column_index,
        min_row_index
    )

    left_down_win_condition_values = get_left_down_condition_values(
        board,
        row_index,
        col_index,
        min_column_index,
        max_row_index
    )

    right_down_win_condition_values = get_right_down_win_condition_values(
        board,
        row_index,
        col_index,
        max_column_index,
        max_row_index
    )

    possible_wins = [
        right_win_condition_values,
        left_win_condition_values,
        up_win_condition_values,
        down_win_condition_values,
        left_up_win_condition_values,
        right_up_win_condition_values,
        left_down_win_condition_values,
        right_down_win_condition_values
    ]
    for values in possible_wins:
        if len(values) == win_count and len(set(values)) == 1:
            return True

    return False


def play(board, win_count):
    current_player, other_player = 1, 2

    while True:
        current_choice = player_choice(current_player)
        if not is_valid_player_choice(current_choice, board):
            print('Invalid column, try again!')
            continue

        player_row, player_col = applying_current_choice(current_player, current_choice, board)
        if check_for_win(board, player_row, player_col, win_count):
            print_board(board)
            print(f'The winner is player {current_player}')
            break

        print_board(board)
        current_player, other_player = other_player, current_player


def create_board(row_count, column_count):
    return [[None] * column_count for _ in range(row_count)]


def print_board(board):
    def get_value(value):
        if value is None:
            return 0
        return value

    for row in board:
        print([get_value(x) for x in row])


created_board = create_board(6, 7)
win_slots_count = 4

play(created_board, win_slots_count)
