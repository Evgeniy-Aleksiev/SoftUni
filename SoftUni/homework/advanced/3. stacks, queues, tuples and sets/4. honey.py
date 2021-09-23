from collections import deque

expression = {
    '*': lambda a, b: a * b,
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
}

bees = deque(map(int, input().split()))
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_bee <= current_nectar:
        symbol = symbols.popleft()
        if symbol == '/':
            try:
                total_honey += abs(current_bee / current_nectar)
            except ZeroDivisionError:
                continue
        else:
            total_honey += abs(expression[symbol](current_bee, current_nectar))
    else:
        bees.appendleft(current_bee)


print(f'Total honey made: {total_honey}')
if bees:
    print(f'Bees left: {", ".join(map(str, bees))}')
if nectar:
    print(f'Nectar left: {", ".join(map(str, nectar))}')
