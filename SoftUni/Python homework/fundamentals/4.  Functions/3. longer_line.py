from math import floor


def first_coordinate(x, y, x1, y1):
    result = abs(x) + abs(y) + abs(x1) + abs(y1)

    return floor(result)


def second_coordinate(x, y, x1, y1):
    result = abs(x) + abs(y) + abs(x1) + abs(y1)

    return floor(result)


fx = float(input())
fy = float(input())
fx1 = float(input())
fy1 = float(input())
sx = float(input())
sy = float(input())
sx1 = float(input())
sy1 = float(input())

first = first_coordinate(fx, fy, fx1, fy1)
second = second_coordinate(sx, sy, sx1, sy1)

if first >= second:
    if abs(fx) + abs(fy) <= abs(fx1) + abs(fy1):
        print(f"({floor(fx)}, {floor(fy)})({floor(fx1)}, {floor(fy1)})")
    else:
        print(f"({floor(fx1)}, {floor(fy1)})({floor(fx)}, {floor(fy)})")
else:
    if abs(sx) + abs(sy) <= abs(sx1) + abs(sy1):
        print(f"({floor(sx)}, {floor(sy)})({floor(sx1)}, {floor(sy1)})")
    else:
        print(f"({floor(sx1)}, {floor(sy1)})({floor(sx)}, {floor(sy)})")