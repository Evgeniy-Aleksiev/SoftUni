from collections import deque

starting_quantity = int(input())
name = input()
queue = deque()

while not name == "Start":
    queue.append(name)

    name = input()

command = input()

while not command == "End":

    if command.startswith("refill"):
        starting_quantity += int(command.split()[-1])
    else:
        water_wants = int(command)
        if water_wants <= starting_quantity:
            print(f"{queue.popleft()} got water")
            starting_quantity -= water_wants
        else:
            print(f"{queue.popleft()} must wait")

    command = input()

print(f"{starting_quantity} liters left")
