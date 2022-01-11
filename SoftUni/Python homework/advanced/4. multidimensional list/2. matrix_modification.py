def invalid_coordinates(matrix_size, r, c):
    return r < 0 or 0 > c or r >= matrix_size or c >= matrix_size


size = int(input())
matrix = []

for current_row in range(size):
    row = [int(x) for x in input().split()]
    matrix.append(row)

while True:
    data = input()

    if data == "END":
        break

    arg = data.split()
    command = arg[0]
    row, col, value = [int(x) for x in arg[1:]]

    if invalid_coordinates(size, row, col):
        print("Invalid coordinates")
        continue

    if command == 'Add':
        matrix[row][col] += value
    elif command == 'Subtract':
        matrix[row][col] -= value

for row in matrix:
    print(*row)
