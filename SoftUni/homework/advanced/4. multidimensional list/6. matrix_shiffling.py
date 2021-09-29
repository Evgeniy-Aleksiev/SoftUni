def is_valid(r, c, row, col):
    return 0 <= r < row and 0 <= c < col


rows_count, columns_count = [int(x) for x in input().split()]

matrix = []

for current_row in range(rows_count):
    matrix.append(input().split())

while True:
    data = input()

    if data == "END":
        break

    arg = data.split()

    if not arg[0] == 'swap' or not len(arg) == 5:
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = [int(x) for x in arg[1:]]

    if not is_valid(row1, col1, rows_count, columns_count) or not is_valid(row2, col2, rows_count, columns_count):
        print('Invalid input!')
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for el in matrix:
        print(' '.join(el))
