matrix = []

for _ in range(int(input())):
    row_input = [int(x) for x in input().split(', ')]
    matrix.append(row_input)

primary_diagonal = []
primary_diagonal_sum = 0

for row in range(len(matrix)):
    num = matrix[row][row]
    primary_diagonal_sum += num
    primary_diagonal.append(num)

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {primary_diagonal_sum}')

secondary_diagonal = []
secondary_diagonal_sum = 0

for row in range(len(matrix)):
    number = matrix[row][len(matrix) - row - 1]
    secondary_diagonal.append(number)
    secondary_diagonal_sum += number

print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {secondary_diagonal_sum}")

