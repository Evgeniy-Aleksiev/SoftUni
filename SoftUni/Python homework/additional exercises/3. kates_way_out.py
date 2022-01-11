def check_if_she_got_out(k_row, k_col, moves_count, board):
    if k_row == len(board) - 1 or k_row == 0 or k_col == len(board[0]) - 1 or k_col == 0:
        print(f"Kate got out in {len(moves_count) + 1} moves")
        return True

    return False


def move(k_row, k_col, board):
    # up
    if board[k_row - 1][k_col] == ' ' and [k_row - 1, k_col] not in previous_positions:
        previous_positions.append([k_row, k_col])
        k_row -= 1

    # down
    elif board[k_row + 1][k_col] == ' ' and [k_row + 1, k_col] not in previous_positions:
        previous_positions.append([k_row, k_col])
        k_row += 1

    # left
    elif board[k_row][k_col - 1] == ' ' and [k_row, k_col - 1] not in previous_positions:
        previous_positions.append([k_row, k_col])
        k_col -= 1

    # right
    elif board[k_row][k_col + 1] == ' ' and [k_row, k_col + 1] not in previous_positions:
        previous_positions.append([k_row, k_col])
        k_col += 1
    else:
        board[k_row][k_col] = '#'
        previous_positions.clear()
        k_row, k_col = starting_row, starting_col

    return k_row, k_col


maze = []
starting_row, starting_col = 0, 0

for row in range(int(input())):
    current_row = list(input())
    maze.append(current_row)
    for col in range(len(current_row)):
        if current_row[col] == 'k':
            starting_row, starting_col = row, col

previous_positions = []
kate_row, kate_col = starting_row, starting_col
got_out = False

while maze[starting_row][starting_col] == 'k':
    kate_row, kate_col = move(kate_row, kate_col, maze)
    got_out = check_if_she_got_out(kate_row, kate_col, previous_positions, maze)
    if got_out:
        got_out = True
        break

if not got_out:
    print("Kate cannot get out")

