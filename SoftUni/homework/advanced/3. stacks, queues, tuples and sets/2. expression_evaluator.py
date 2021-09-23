from collections import deque

expression = {
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
}
input_line = input().split()
numbers = deque()
result = 0

for el in input_line:
    if el in expression:
        result = numbers.popleft()
        while numbers:
            number = numbers.popleft()
            result = expression[el](result, number)
        numbers.appendleft(result)
    else:
        numbers.append(int(el))

print(numbers.popleft())
