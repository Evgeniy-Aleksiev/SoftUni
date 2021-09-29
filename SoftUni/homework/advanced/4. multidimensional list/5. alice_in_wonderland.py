def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_next_position(r, c, cmd):
    if cmd == 'up':
        return r - 1, c
    if cmd == 'down':
        return r + 1, c
    if cmd == 'right':
        return r, c + 1
    if cmd == 'left':
        return r, c - 1


matrix_size = int(input())
matrix = []
alice_row, alice_col = 0, 0
total_tea = 0

for row in range(matrix_size):
    matrix.append(input().split())
    for col in range(matrix_size):
        if matrix[row][col] == 'A':
            alice_row, alice_col = row, col

while True:
    command = input()
    matrix[alice_row][alice_col] = '*'

    alice_row, alice_col = get_next_position(alice_row, alice_col, command)
    if is_valid(matrix_size, alice_row, alice_col):
        position = matrix[alice_row][alice_col]
        matrix[alice_row][alice_col] = '*'
        if position == 'R':
            break
        elif position.isdigit():
            total_tea += int(position)
            if total_tea >= 10:
                break
    else:
        break

if total_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row)
