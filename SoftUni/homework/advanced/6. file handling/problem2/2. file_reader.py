file = open('numbers.txt', 'r')
result = sum(map(int, file))
print(result)

file.close()

file = open('numbers.txt', 'r')
result = 0

for number in file:
    result += int(number)

print(result)
file.close()