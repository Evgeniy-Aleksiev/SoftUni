from collections import deque

cups_capacity = deque(map(int, input().split()))
filled_bottles = deque(map(int, input().split()))

wasted_water = 0

while filled_bottles and cups_capacity:
    current_cup = cups_capacity[0]
    current_bottle = filled_bottles.pop()

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
        cups_capacity.popleft()

    else:
        cups_capacity[0] = current_cup - current_bottle

if cups_capacity:
    print(f"Cups: {' '.join(map(str, cups_capacity))}")
elif filled_bottles:
    print(f"Bottles: {' '.join(map(str, filled_bottles))}")

print(f"Wasted litters of water: {wasted_water}")

