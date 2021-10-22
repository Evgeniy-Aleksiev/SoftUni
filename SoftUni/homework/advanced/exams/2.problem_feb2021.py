def is_valid(r, c, matrix_size):
    return 0 <= r < matrix_size and 0 <= c < matrix_size


def create_matrix(size):
    player_r, player_c = 0, 0
    matrix = []

    for r in range(size):
        current_row = input().split()
        matrix.append(current_row)
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'P':
                player_r, player_c = r, c

    return player_r, player_c, matrix


def commands(r, c, command):
    if command == 'up':
        return r - 1, c
    if command == 'down':
        return r + 1, c
    if command == 'left':
        return r, c - 1
    if command == 'right':
        return r, c + 1


def play(matrix, r, c, size):
    current_r, current_c = r, c
    coins = 0
    coordinates = []
    won = None

    while True:
        command = input()
        try:
            new_row, new_col = commands(current_r, current_c, command)
        except TypeError:
            continue
        if not is_valid(new_row, new_col, size):
            won = False
            break

        if matrix[new_row][new_col] == 'X':
            won = False
            break

        current_r, current_c = new_row, new_col
        coordinates.append([current_r, current_c])
        coins += int(matrix[new_row][new_col])
        if coins >= 100:
            won = True
            break

    return coins, coordinates, won


matrix_size = int(input())
player_row, player_col, field = create_matrix(matrix_size)
total_coins, coordinates, won = play(field, player_row, player_col, matrix_size)

if won:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {round(total_coins // 2)} coins.")

print("Your path: ")
[print(cord)for cord in coordinates]
