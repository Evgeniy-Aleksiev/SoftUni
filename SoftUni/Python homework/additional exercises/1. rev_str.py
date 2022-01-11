text = list(input())
result = []

for _ in range(len(text)):
    result.append(text.pop())

print(''.join(result))
