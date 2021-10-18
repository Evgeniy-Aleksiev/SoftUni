even_number = []

for row_i in range(int(input())):
    row = [int(x) for x in input().split(', ')]
    even = [x for x in row if x % 2 == 0]
    even_number.append(even)
print(even_number)