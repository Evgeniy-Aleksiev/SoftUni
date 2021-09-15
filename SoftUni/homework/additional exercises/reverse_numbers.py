numbers, rev = list(input()), []

for num in range(len(numbers)):
    rev.append(numbers.pop())

print(''.join(rev))
