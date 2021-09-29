def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_houses_in_range(size, r, c):
    houses_cord = []
    if is_valid(size, r - 1, c):           # up
        houses_cord.append([r - 1, c])
    if is_valid(size, r + 1, c):           # down
        houses_cord.append([r + 1, c])
    if is_valid(size, r, c + 1):           # right
        houses_cord.append([r, c + 1])
    if is_valid(size, r, c - 1):           # left
        houses_cord.append([r, c - 1])

    return houses_cord


def get_next_position(r, c, cmd):
    if cmd == 'up':
        return r - 1, c
    if cmd == 'down':
        return r + 1, c
    if cmd == 'right':
        return r, c + 1
    if cmd == 'left':
        return r, c - 1


count_of_presents = int(input())
matrix_size = int(input())
matrix = []
good_kids_count = 0
total_good_kids = 0
santa_row, santa_col = 0, 0

for row in range(matrix_size):
    matrix.append(input().split())
    for col in range(matrix_size):
        element = matrix[row][col]
        if matrix[row][col] == 'S':
            santa_row, santa_col = row, col
        elif matrix[row][col] == 'V':
            total_good_kids += 1

while True:
    command = input()

    if command == 'Christmas morning':
        break

    next_row, nex_col = get_next_position(santa_row, santa_col, command)
    if not is_valid(matrix_size, next_row, nex_col):
        continue

    if matrix[next_row][nex_col] == 'V':
        good_kids_count += 1
        count_of_presents -= 1

    elif matrix[next_row][nex_col] == 'C':
        houses_in_range = get_houses_in_range(matrix_size, next_row, nex_col)
        for row, col in houses_in_range:
            if matrix[row][col] == 'V':
                good_kids_count += 1
                count_of_presents -= 1
            elif matrix[row][col] == 'X':
                count_of_presents -= 1
            matrix[row][col] = '-'
            if count_of_presents == 0:
                break

    matrix[santa_row][santa_col] = '-'
    matrix[next_row][nex_col] = 'S'
    santa_row, santa_col = next_row, nex_col
    if count_of_presents == 0:
        break

if count_of_presents == 0 and total_good_kids - good_kids_count > 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row)

if total_good_kids == good_kids_count:
    print(f"Good job, Santa! {total_good_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_good_kids - good_kids_count} nice kid/s.")

