text = list(input())
reverse = []

while len(text) > 0:
    reverse.append(text.pop())

print(''.join(reverse))
