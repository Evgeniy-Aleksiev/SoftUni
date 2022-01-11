from collections import deque

petrol_amount = int(input())
pumps = deque()

for _ in range(petrol_amount):
    command = [int(x) for x in input().split()]
    pumps.append(command)

for index in range(petrol_amount):
    fuel = 0
    completed = True

    for petrol, distance in pumps:
        fuel += petrol

        if distance > fuel:
            completed = False
            break
        fuel -= distance

    if completed:
        print(index)
        break
    pumps.append(pumps.popleft())
