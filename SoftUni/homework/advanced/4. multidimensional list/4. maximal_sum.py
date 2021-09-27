import sys


def read_matrix():
    matrix = []

    rows_count, columns_count = [int(x) for x in input().split()]

    for current_row in range(rows_count):
        row = [int(x) for x in input().split()]
        matrix.append(row)

    return matrix, rows_count, columns_count


matrix, rows, cols = read_matrix()
max_sum = -sys.maxsize
best_r = 0
best_c = 0

for r in range(rows - 2):
    for c in range(cols - 2):
        current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] +\
            matrix[r + 1][c] + matrix[r + 1][c + 1] + matrix[r + 1][c + 2] +\
            matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            best_r = r
            best_c = c

print(f'Sum = {max_sum}')
for r in range(best_r, best_r + 3):
    for c in range(best_c, best_c + 3):
        print(f"{matrix[r][c]}", end=' ')
    print()
