row, col = input().split(', ')
matrix = []
sum_of_numbers = 0

for _ in range(int(row)):
    numbers = [int(x) for x in input().split(', ')]
    sum_of_numbers += sum(numbers)
    matrix.append(numbers)

print(sum_of_numbers)
print(matrix)