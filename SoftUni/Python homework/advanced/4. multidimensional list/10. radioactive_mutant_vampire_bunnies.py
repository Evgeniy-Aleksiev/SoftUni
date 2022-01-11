def is_valid(cur_row, cur_col, r, c):
    return 0 <= r < cur_row and 0 <= c < cur_col


def bunny_positions_finder(matrix, rows, cols):
    bunny_finder = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'B':
                bunny_finder.append([r, c])
    return bunny_finder


def bunny_spreads(matrix, current_bunny_positions):
    is_killed = False
    for bunny_row, bunny_col in current_bunny_positions:
        for index in movement_operator.values():
            new_r = bunny_row + index[0]
            new_c = bunny_col + index[1]
            if is_valid(len(matrix), len(matrix[bunny_row]), new_r, new_c):
                if matrix[new_r][new_c] == 'P':
                    is_killed = True
                matrix[new_r][new_c] = 'B'

    return matrix, is_killed


movement_operator = {
    'L': [0, -1],
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0]
    }

matrix = []
player_position = None
is_dead = False
is_won = False

rows_count, columns_count = [int(x) for x in input().split()]

for row in range(rows_count):
    matrix.append(list(input()))
    for col in range(columns_count):
        if matrix[row][col] == 'P':
            player_position = (row, col)

commands = input()

for command in commands:
    current_row, current_col = player_position
    row_ind_to_add, col_ind_to_add = movement_operator[command]
    new_row = current_row + row_ind_to_add
    new_col = current_col + col_ind_to_add
    matrix[current_row][current_col] = '.'

    if is_valid(rows_count, columns_count, new_row, new_col):
        player_position = (new_row, new_col)
        matrix[new_row][new_col] = 'P'
        matrix, is_dead = bunny_spreads(matrix, bunny_positions_finder(matrix, rows_count, columns_count))
        if is_dead:
            break
    else:
        is_won = True
        matrix, is_dead = bunny_spreads(matrix, bunny_positions_finder(matrix, rows_count, columns_count))
        break

for row in matrix:
    print(''.join(row))
if is_dead:
    print(f'dead: {" ".join(str(x) for x in player_position)}')
if is_won:
    print(f'won: {" ".join(str(x) for x in player_position)}')
