def read_matrix2():
    matrix = []
    total_sum = 0

    for row in range(int(input())):
        current_row = [int(x) for x in input().split()]
        matrix.append(current_row)
        total_sum += matrix[row][row]

    return total_sum


print(read_matrix2())


matrix = []
total_sum = 0

for row in range(int(input())):
    matrix.append([int(x) for x in input().split()])
    total_sum += matrix[row][row]

print(total_sum)