from math import ceil

height = int(input())
width = int(input())
not_painted = int(input())
total_room_size = height * width * 4
need_to_paint = ceil(total_room_size - (not_painted / 100 * total_room_size))

total_paint = 0
command = input()
while command != "Tired!":
    paint = int(command)
    total_paint += paint
    if total_paint >= need_to_paint:
        break
    command = input()

difference = abs(need_to_paint - total_paint)
if command == "Tired!":
    print(f"{difference} quadratic m left." )
elif total_paint == need_to_paint:
    print(f"All walls are painted! Great job, Pesho!" )
elif total_paint > need_to_paint:
    print(f"All walls are painted and you have {difference} l paint left!" )
