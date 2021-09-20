from collections import deque

numbers = deque(map(int, input().split()))
rack_capacity = int(input())
racks = 0
box_sum = 0

for i in range(len(numbers)):
    box = numbers.popleft()

    if box + box_sum <= rack_capacity:
        box_sum += box
    else:
        racks += 1
        box_sum = box

    if len(numbers) == 0:
        racks += 1

print(racks)