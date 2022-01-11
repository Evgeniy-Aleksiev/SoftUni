numbers = input().split()
rev = []

for n in range(len(numbers)):
    rev.append(numbers.pop())

print(' '.join(rev))
