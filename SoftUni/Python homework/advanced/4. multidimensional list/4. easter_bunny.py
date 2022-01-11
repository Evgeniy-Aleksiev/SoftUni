def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


possible_moves = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

matrix_size = int(input())
matrix = []
bunny_row, bunny_col = 0, 0

for row in range(matrix_size):
    matrix.append(input().split())
    for col in range(matrix_size):
        if matrix[row][col] == 'B':
            bunny_row, bunny_col = row, col

best_direction, best_coordinates, max_eggs = '', [], float('-inf')

for direction, move_index in possible_moves.items():
    current_row, current_col = bunny_row, bunny_col
    eggs_collected, current_coordinates = 0, []

    while True:
        current_row, current_col = move_index(current_row, current_col)
        if not is_valid(matrix_size, current_row, current_col):
            break
        if matrix[current_row][current_col] == 'X':
            break
        eggs_collected += int(matrix[current_row][current_col])
        current_coordinates.append([current_row, current_col])

    if eggs_collected > max_eggs:
        best_direction, best_coordinates, max_eggs = direction, current_coordinates, eggs_collected

print(best_direction)
for cor in best_coordinates:
    print(cor)
print(max_eggs)