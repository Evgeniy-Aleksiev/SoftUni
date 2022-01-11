def read_matrix1():
    matrix = []
    row_count, columns_count = map(int, input().split(', '))

    for row in range(row_count):
        matrix.append([])
        for col in range(1, columns_count):
            matrix[row].append(col)
    return matrix


print(read_matrix1())


def read_matrix2():
    matrix = []
    row_count, columns_count = map(int, input().split(', '))

    for row in range(row_count):
        columns = [int(x) for x in range(1, columns_count)]
        matrix.append(columns)

    return matrix


print(read_matrix2())

matrix = []
for i in range(3):
    matrix.append([])
    for j in range(1, 4):
        matrix[i].append(j)

print(matrix)

mat = [[j for j in range(1, 4)] for i in range(3)]
print(mat)
