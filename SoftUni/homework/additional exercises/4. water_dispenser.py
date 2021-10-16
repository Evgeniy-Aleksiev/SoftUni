from collections import deque

water_quantity = int(input())
names = input()
queue = deque()

while not names == 'Start':
    queue.append(names)
    names = input()

while True:
    command = input()
    if command == 'End':
        break

    if 'refill' in command:
        _, litters = command.split()
        water_quantity += int(litters)
        continue

    litters = int(command)
    person = queue.popleft()

    if litters > water_quantity:
        print(person, "must wait")
        continue

    water_quantity -= litters
    print(person, "got water")

print(water_quantity, "liters left")