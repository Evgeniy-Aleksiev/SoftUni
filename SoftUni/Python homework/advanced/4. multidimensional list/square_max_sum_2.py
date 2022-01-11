import sys

def read_matrix():
    matrix = []
    rows_count, columns_count = [int(x) for x in input().split(', ')]

    for current_row in range(rows_count):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)

    return matrix, rows_count, columns_count


matrix, rows, columns = read_matrix()
max_sum = -sys.maxsize
best_row = 0
best_col = 0

for r in range(rows - 1):
    for c in range(columns - 1):
        current_sum = matrix[r][c] + matrix[r][c + 1] +\
                      matrix[r + 1][c] + matrix[r + 1][c + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            best_row = r
            best_col = c

print(matrix[best_row][best_col], matrix[best_row][best_col + 1])
print(matrix[best_row + 1][best_col], matrix[best_row + 1][best_col + 1])
print(max_sum)
