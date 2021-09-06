width = int(input())
length = int(input())
height = int(input())
box_size = width * length * height
box_count = 0
no_free_space = False

command = input()

while command != "Done":
    box_number = int(command)
    box_count += box_number
    if box_count > box_size:
        no_free_space = True
        break
    else:
        command = input()

difference = abs(box_size - box_count)
if no_free_space:
    print(f"No more free space! You need {difference} Cubic meters more.")
else:
    print(f"{difference} Cubic meters left.")