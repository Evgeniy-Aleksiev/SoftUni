row_cnt, col_cnt = [int(x) for x in input().split()]
matrix = []

for _ in range(row_cnt):
    row_numbers = [int(x) for x in input().split()]
    matrix.append(row_numbers)

best_sum = 0
best_row, best_col = 0, 0

for row in range(row_cnt - 2):
    for col in range(col_cnt - 2):
        current_move_sum = 0
        for current_row in range(row, row + 3):
            for current_col in range(col, col + 3):
                current_move_sum += matrix[current_row][current_col]
        if current_move_sum > best_sum:
            best_sum = current_move_sum
            best_row, best_col = row, col

print(best_sum)
for r in range(best_row, best_row + 3):
    for c in range(best_col, best_col + 3):
        print(f"{matrix[r][c]}", end=' ')
    print()