def is_valid(matrix, r, c, cmd):
    if cmd == 'left':
        if 0 <= r < len(matrix) and 0 <= c - 1 < len(matrix):
            return r, c - 1
    elif cmd == 'right':
        if 0 <= r < len(matrix) and 0 <= c + 1 < len(matrix):
            return r, c + 1
    elif cmd == 'up':
        if 0 <= r - 1 < len(matrix) and 0 <= c < len(matrix):
            return r - 1, c
    elif cmd == 'down':
        if 0 <= r + 1 < len(matrix) and 0 <= c < len(matrix):
            return r + 1, c

    return r, c


matrix = []
matrix_size = int(input())
commands = input().split()

miner_position = None
coals_count = 0

for row in range(matrix_size):
    matrix.append(input().split())
    for col in range(matrix_size):
        if matrix[row][col] == 's':
            miner_position = (row, col)
        if matrix[row][col] == 'c':
            coals_count += 1

for command in commands:
    r, c = miner_position
    row, col = is_valid(matrix, r, c, command)

    if matrix[row][col] != 's':
        matrix[r][c] = '*'
        miner_position = (row, col)

        if matrix[row][col] == 'e':
            print(f"Game over! {miner_position}")
            exit()
        if matrix[row][col] == 'c':
            coals_count -= 1
            if coals_count == 0:
                print(f"You collected all coal! {miner_position}")
                exit()
        matrix[row][col] = 's'

print(f"{coals_count} pieces of coal left. {miner_position}")
