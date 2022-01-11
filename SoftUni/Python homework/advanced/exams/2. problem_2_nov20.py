def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


def commands(command, r, c):
    if command == 'up':
        return r - 1, c
    elif command == 'down':
        return r + 1, c
    elif command == 'left':
        return r, c - 1
    elif command == 'right':
        return r, c + 1


def get_matrix():
    matrix_size = int(input())
    matrix = []
    player_row, player_col = 0, 0

    for row in range(matrix_size):
        current_row = list(input())
        matrix.append(current_row)
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'P':
                player_row, player_col = row, col

    return matrix, player_row, player_col


def play(board, p_r, p_c, letter):
    current_row, current_col = p_r, p_c

    for _ in range(int(input())):
        command = input()
        r, c = commands(command, current_row, current_col)
        if not is_valid(len(board), r, c):
            if letter:
                letter = letter[:-1]
            continue

        if not board[r][c] == '-':
            letter += board[r][c]

        board[r][c] = 'P'
        board[current_row][current_col] = '-'
        current_row, current_col = r, c

    return board, letter


initial_string = input()
board, player_r, player_c = get_matrix()
board, initial_string = play(board, player_r, player_c, initial_string)

print(initial_string)
[print(''.join(row)) for row in board]