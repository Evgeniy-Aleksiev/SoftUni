row_cnt, col_cnt = [int(x) for x in input().split()]
matrix = []

for _ in range(row_cnt):
    matrix.append(input().split())

squares_found = 0

for row in range(row_cnt - 1):
    for col in range(col_cnt - 1):
        if matrix[row][col] == matrix[row][col + 1] ==\
                matrix[row + 1][col] == matrix[row + 1][col + 1]:
            squares_found += 1

print(squares_found)