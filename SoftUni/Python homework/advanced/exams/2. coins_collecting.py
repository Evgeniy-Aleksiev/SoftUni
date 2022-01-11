def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


def commands(board, r, c, command):
    if command == 'up':
        return r -1, c
    if command == 'down':
        return r +1, c
    if command == 'left':
        return r, c -1
    if command == 'right':
        return r, c +1


def get_board():
    matrix = []
    player_row, player_col = 0, 0

    for row in range(int(input())):
        current_row = input().split()
        matrix.append(current_row)
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'P':
                player_row, player_col = row, col

    return matrix, player_row, player_col


def play(board, player_row, player_col):
    collected_coins = 0
    coordinates = []

    while True:
        command = input()
        row, col = commands(board, player_row, player_col, command)

        if not is_valid(len(board), row, col):
            collected_coins = round(collected_coins // 2)
            break

        if board[row][col] == 'X':
            collected_coins = round(collected_coins // 2)
            break
        player_row, player_col = row, col
        coordinates.append([row, col])
        collected_coins += int(board[row][col])

        if collected_coins >= 100:
            break

    return collected_coins, coordinates


board, player_r, player_c = get_board()
total_coins, coords = play(board, player_r, player_c)

if total_coins >= 100:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {total_coins} coins.")
print('Your path:')
[print(path) for path in coords]