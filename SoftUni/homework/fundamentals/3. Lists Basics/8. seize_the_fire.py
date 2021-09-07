cells_of_fire = input().split("#")
water = int(input())

effort = 0
total_fire = 0
cells_value = []

for cell in cells_of_fire:
    current_cell = cell.split(" = ")
    type_of_fire = current_cell[0]
    cell_value = int(current_cell[1])

    if type_of_fire == "High" and cell_value <= water:
        if 81 <= cell_value <= 125:
            water -= cell_value
            effort += cell_value * 0.25
            total_fire += cell_value
            cells_value.append(cell_value)

    elif type_of_fire == "Medium" and cell_value <= water:
        if 51 <= cell_value <= 80:
            water -= cell_value
            effort += cell_value * 0.25
            total_fire += cell_value
            cells_value.append(cell_value)

    elif type_of_fire == "Low" and cell_value <= water:
        if 1 <= cell_value <= 50:
            water -= cell_value
            effort += cell_value * 0.25
            total_fire += cell_value
            cells_value.append(cell_value)

print("Cells:")
for loop_ceil in cells_value:
    print(f" - {loop_ceil}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")