def is_valid(board, r, c):
    if 0 <= r < len(board) and 0 <= c < len(board[r]):
        return True


def get_coordinates():
    coord_input = input()
    r, c = coord_input[1:-1].split(',')
    return int(r), int(c)


def sum_of_deducted_points(board, r, c):
    coordinates = board[r][c]

    if coordinates.isdigit():
        return int(coordinates)

    sum_of_points = int(board[r][0]) + int(board[r][-1]) + \
                    int(board[0][c]) + int(board[-1][c])
    if coordinates == 'D':
        return sum_of_points * 2
    elif coordinates == 'T':
        return sum_of_points * 3
    elif coordinates == 'B':
        return 501


def play(board, first_player, second_player):
    current_player = first_player, 501, 0
    other_player = second_player, 501, 0

    while True:
        name, points, throw_cnt = current_player
        throw_cnt += 1
        row_command, col_command = get_coordinates()
        if is_valid(board, row_command, col_command):
            points -= sum_of_deducted_points(board, row_command, col_command)

        current_player = (name, points, throw_cnt)

        if points <= 0:
            break

        current_player, other_player = other_player, current_player

    name, _, throw_cnt = current_player
    return f'{name} won the game with {throw_cnt} throws!'



first_player_name, second_player_name = input().split(', ')
matrix_size = 7
matrix = [input().split() for x in range(matrix_size)]

print(play(matrix, first_player_name, second_player_name))