matrix = []

for _ in range(int(input())):
    matrix_row = [int(x) for x in input().split(', ')]
    matrix += matrix_row

print(matrix)