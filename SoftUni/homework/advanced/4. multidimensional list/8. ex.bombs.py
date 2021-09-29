matrix = []
matrix_size = int(input())
alive_cells = 0
alive_cells_sum = 0

for row in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

bomb_coordinates = [[int(n) for n in c.split(",")] for c in input().split()]

for row, col in bomb_coordinates:
    if matrix[row][col] <= 0:
        continue

    bomb_strength = matrix[row][col]
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r in range(len(matrix)) and c in range(len(matrix[r])) and matrix[r][c] > 0:
                matrix[r][c] -= bomb_strength

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            alive_cells_sum += el

print(f'Alive cells: {alive_cells}')
print(f'Sum: {alive_cells_sum}')

for row in matrix:
    print(*row)
