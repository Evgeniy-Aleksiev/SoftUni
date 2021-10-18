matrix = []

for _ in range(int(input())):
    row_numbers = [int(x) for x in input().split()]
    matrix.append(row_numbers)

coordinates = [[int(n) for n in c.split(',')] for c in input().split()]

for row_coord, col_coord in coordinates:
    if matrix[row_coord][col_coord] <= 0:
        continue

    bomb_strenght = matrix[row_coord][col_coord]
    for r in range(row_coord - 1, row_coord + 2):
        for c in range(col_coord - 1, col_coord + 2):
            if r in range(len(matrix)) and c in range(len(matrix[r])) and matrix[r][c] > 0:
                matrix[r][c] -= bomb_strenght

alive_cells = 0
alive_cells_sum = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            alive_cells_sum += el

print(f'Alive cells: {alive_cells}')
print(f'Sum: {alive_cells_sum}')

for row in matrix:
    print(*row)
