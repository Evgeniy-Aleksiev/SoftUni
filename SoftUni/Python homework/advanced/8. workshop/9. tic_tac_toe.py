from errors import InvalidPositionError


def get_first_player_sign(p1):
    while True:
        sign = input(f"{p1} would you like to play with 'X' or 'O'?").upper()

        if not sign == 'X' and not sign == 'O':
            print("The sign should be 'X' or 'O'!")
            continue

        return sign


def read_player_info():
    player_one = input('Player one name: ')
    player_two = input('Player two name: ')

    first_player_sign = get_first_player_sign(player_one)
    second_player_sign = 'X' if first_player_sign == 'O' else 'O'

    return [player_one, first_player_sign], [player_two, second_player_sign]


def print_board_numeration(p1):
    print('This is the numeration of the board:')
    print(
        "|  1  |  2  |  3  |\n"
        "|  4  |  5  |  6  |\n"
        "|  7  |  8  |  9  |"
          )
    print(p1[0], 'starts first!')


def get_play_coordinates(player, board):
    while True:
        try:
            coord = int(input(f'{player} choose a free position [1-9]: '))

            if coord < 1 or coord > 9:
                raise InvalidPositionError(f'{coord} is invalid position.')

            row, col = board_positions(coord)
            position = board[row][col]

            if not position == " ":
                print('The position is already taken')
                continue
            return row, col

        except ValueError:
            print('Please provide a valid position in range [1-9]')
        except InvalidPositionError as error:
            print(error)


def board_positions(coord):
    if coord == 1:
        return 0, 0
    if coord == 2:
        return 0, 1
    if coord == 3:
        return 0, 2
    if coord == 4:
        return 1, 0
    if coord == 5:
        return 1, 1
    if coord == 6:
        return 1, 2
    if coord == 7:
        return 2, 0
    if coord == 8:
        return 2, 1
    if coord == 9:
        return 2, 2


def display_board(board):
    for row in board:
        print("|  ", end='')
        print('  |  '.join(row), end='')
        print('  |')


def is_board_full(board):
    for row in board:
        is_row_full = all([el != ' ' for el in row])
        if not is_row_full:
            return False
    return True


def has_player_won(board, player_sign):
    # horizontal
    for row in board:
        if all([el == player_sign for el in row]):
            return True

    # vertical
    for col in range(len(board)):
        won = True
        for row in range(len(board)):
            if not board[row][col] == player_sign:
                won = False
                break
        if won:
            return True

    # primary diagonal
    won = True
    for idx in range(len(board)):
        if not board[idx][idx] == player_sign:
            won = False
            break
    if won:
        return True

    # secondary diagonal
    won = True
    for idx in range(len(board)):
        if not board[idx][len(board) - 1 - idx] == player_sign:
            won = False
            break

    return won


def play(board, p1, p2):
    current_play, other_play = p1, p2
    while True:
        current_player, current_sign = current_play[0], current_play[1]

        row, col = get_play_coordinates(current_player, board)
        board[row][col] = current_sign
        display_board(board)
        if has_player_won(board, current_sign):
            print(current_player, 'won!')
            break

        if is_board_full(board):
            print('Draw!')
            break

        current_play, other_play = other_play, current_play


player1, player2 = read_player_info()

print_board_numeration(player1)

get_board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

play(get_board, player1, player2)
