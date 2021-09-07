from math import floor


def coordinate(x, y):
    result = abs(x) + abs(y)

    return floor(result)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

first_coordinate = coordinate(x1, y1)
second_coordinate = coordinate(x2, y2)

if first_coordinate <= second_coordinate:
    print(f"({floor(x1)}, {floor(y1)})")
else:
    print(f"({floor(x2)}, {floor(y2)})")