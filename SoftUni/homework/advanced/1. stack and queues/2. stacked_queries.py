stack = []
rev = []

for _ in range(int(input())):
    queries = input()

    if queries.startswith("1"):
        number = int(queries.split()[-1])
        stack.append(number)
    if len(stack) > 0:
        if queries == "2":
            stack.pop()
        elif queries == "3":
            print(max(stack))
        elif queries == "4":
            print(min(stack))

for _ in range(len(stack)):
    rev.append(str(stack.pop()))

print(', '.join(rev))

