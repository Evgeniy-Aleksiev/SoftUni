from math import pi

type = input()

if type == "square":
    side = float(input())
    area = side ** 2
    print(f"{area:.03f}")
elif type == "rectangle":
    width = float(input())
    side = float(input())
    area = width * side
    print(f"{area:.03f}")
elif type == "circle":
    radius = float(input())
    area = radius ** 2 * pi
    print(f"{area:.03f}")
elif type == "triangle":
    width_side = float(input())
    width_height = float(input())
    area = width_side * width_height / 2
    print(f"{area:.03f}")