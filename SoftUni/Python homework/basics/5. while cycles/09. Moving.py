width = int(input())
length = int(input())
height = int(input())
box_size = width * length * height
box_count = 0
free_space = False

while box_count < box_size:
    command = input()
    if command == "Done":
        free_space = True
        break
    else:
        box_number = int(command)
        box_count += box_number

difference = abs(box_count - box_size)
if free_space or box_size > box_count:
    print(f"{difference} Cubic meters left.")
else:
    print(f"No more free space! You need {difference} Cubic meters more.")
