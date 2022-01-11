def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_next_position(r, c, cmd, num_steps=1):
    if cmd == 'up':
        return r - num_steps, c
    if cmd == 'down':
        return r + num_steps, c
    if cmd == 'right':
        return r, c + num_steps
    if cmd == 'left':
        return r, c - num_steps


matrix_size = 5
matrix = []
player_row, player_col = 0, 0
target_count = 0
total_hit_targets = 0
hit_targets_cords = []

for row in range(matrix_size):
    matrix.append(input().split())
    for col in range(matrix_size):
        if matrix[row][col] == 'A':
            player_row, player_col = row, col
        elif matrix[row][col] == 'x':
            target_count += 1

for _ in range(int(input())):
    cmd = input().split()
    command, direction = cmd[0], cmd[1]

    if command == 'move':
        steps = int(cmd[2])
        new_row, new_col = get_next_position(player_row, player_col, direction, steps)
        if is_valid(matrix_size, new_row, new_col) and matrix[new_row][new_col] == '.':
            matrix[player_row][player_col] = '.'
            player_row, player_col = new_row, new_col
            matrix[new_row][new_col] = 'A'

    elif command == 'shoot':
        bullet_row, bullet_col = get_next_position(player_row, player_col, direction)

        while True:
            if not is_valid(matrix_size, bullet_row, bullet_col):
                break

            if matrix[bullet_row][bullet_col] == 'x':
                total_hit_targets += 1
                hit_targets_cords.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = '.'
                break
            bullet_row, bullet_col = get_next_position(bullet_row, bullet_col, direction)

        if total_hit_targets == target_count:
            break

if total_hit_targets == target_count:
    print(f"Training completed! All {target_count} targets hit.")
else:
    print(f"Training not completed! {target_count - total_hit_targets} targets left.")

for cord in hit_targets_cords:
    print(cord)