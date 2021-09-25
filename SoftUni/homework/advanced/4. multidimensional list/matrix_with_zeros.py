def read_matrix():
    matrix = []
    row_count, columns_count = map(int, input().split(', '))
    for row in range(row_count):
        matrix.append([])
        for col in range(columns_count):
            matrix[row].append(0)

    return matrix


print(read_matrix())


def read_matrix2():
    matrix = []
    row_count, columns_count = map(int, input().split(', '))
    for row in range(row_count):
        matrix.append([0] * columns_count)

    return matrix


print(read_matrix2())

matrix = []
for i in range(3):
    matrix.append([])
    for j in range(2):
        matrix[i].append(0)
print(matrix)

mat = [[0 for j in range(2)] for i in range(3)]
print(mat)