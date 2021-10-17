from collections import deque

commands = deque()
completed = False
index = 0

for _ in range(int(input())):
     commands.append([int(x) for x in input().split()])

while not completed:
    total_petrol_amount = 0
    for petrol_amount, distance in commands:
        if petrol_amount + total_petrol_amount >= distance:
            completed = True
            total_petrol_amount += petrol_amount - distance
        else:
            completed = False
            commands.append(commands.popleft())
            break

    if completed:
        print(index)
    index += 1
