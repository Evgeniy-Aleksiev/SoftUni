def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_board():
    matrix = []
    snake_row, snake_col = 0, 0
    burrows = []

    for row in range(int(input())):
        matrix.append(list(input()))
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'S':
                snake_row, snake_col = row, col
            elif matrix[row][col] == 'B':
                current_burrow = (row, col)
                burrows.append(current_burrow)

    return matrix, snake_row, snake_col, burrows


def move_commands(command, r, c):
    if command == 'up':
        return r - 1, c
    if command == 'down':
        return r + 1, c
    if command == 'left':
        return r, c - 1
    if command == 'right':
        return r, c + 1


def play(board, row, col, burrows_coordinates):
    food_quantity = 0

    while True:
        command = input()
        new_row, new_col = move_commands(command, row, col)

        if not is_valid(len(board), new_row, new_col):
            board[row][col] = '.'
            break

        position = board[new_row][new_col]
        board[row][col] = '.'

        if position == '*':
            food_quantity += 1

        if position == 'B':
            burrows_coordinates.remove((new_row, new_col))
            board[new_row][new_col] = '.'
            r = burrows_coordinates[-1][0]
            c = burrows_coordinates[-1][1]
            board[r][c] = 'S'
            row, col = r, c
            continue

        board[new_row][new_col] = 'S'
        row, col = new_row, new_col
        if food_quantity >= 10:
            break

    return board, food_quantity


board, snake_r, snake_c, burrows = get_board()
board, food = play(board, snake_r, snake_c, burrows)

if food >= 10:
    print("You won! You fed the snake.")
else:
    print("Game over!")

print(f"Food eaten: {food}")
[print(''.join(row)) for row in board]