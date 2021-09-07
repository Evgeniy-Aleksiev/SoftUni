water_tank = int(input())
capacity = 255
tank = 0
tank_is_full = False
for litters_of_water in range(water_tank):
    current_fill = int(input())
    if current_fill > capacity:
        print("Insufficient capacity!")
    else:
        capacity -= current_fill
        tank += current_fill
print(tank)