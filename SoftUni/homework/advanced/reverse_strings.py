text = list(input())
rev = []

for i in range(len(text)):
    rev.append(text.pop())

print(''.join(rev))