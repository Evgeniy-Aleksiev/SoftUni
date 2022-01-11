# Изчислява обема на кораба, колко астронавта ще събере и принтира дали кораба е достатъчно голям
# Място за астронавти -> поне 3ма, но не повече от 10
# Всеки астронавт се нуждае от 2 метра ширина, 2м дължина и височина, която е с 40 см повече от средната вис
import math

width = float(input())
length = float(input())
height = float(input())
average_height_of_astronauts = float(input())

rocket_volume = width * length * height
room_volume = (average_height_of_astronauts + 0.40) * 2 * 2
space_for_astronauts = math.floor(rocket_volume / room_volume)

if space_for_astronauts < 3:
    print("The spacecraft is too small.")
elif space_for_astronauts > 10:
    print("The spacecraft is too big.")
else:
    print(f"The spacecraft holds {space_for_astronauts} astronauts.")
