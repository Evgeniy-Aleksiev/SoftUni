from collections import deque

quantity = int(input())
name = input()
queue = deque()

while not name == "Start":
    queue.append(name)

    name = input()

command = input()

while not command == "End":

    if command.startswith("refill"):
        quantity += int(command.split()[-1])
    else:
        liters = int(command)
        name = queue.popleft()
        if quantity >= liters:
            print(f"{name} got water")
            quantity -= liters
        else:
            print(f"{name} must wait")

    command = input()

print(f"{quantity} liters left")