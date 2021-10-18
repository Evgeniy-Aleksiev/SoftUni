matrix = []
row_cnt, col_cnt = [int(x) for x in input().split(', ')]

for _ in range(row_cnt):
    row_numbers = [int(x) for x in input().split(', ')]
    matrix.append(row_numbers)

biggest_sum = 0
best_row, best_col = 0, 0
for row in range(row_cnt -1):
    for col in range(col_cnt -1):
        current_sum = matrix[row][col] + matrix[row][col + 1] +\
                matrix[row + 1][col] + matrix[row+1][col + 1]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            best_row, best_col = row, col

print(matrix[best_row][best_col], matrix[best_row][best_col + 1])
print(matrix[best_row + 1][best_col], matrix[best_row + 1][best_col + 1])
print(biggest_sum)