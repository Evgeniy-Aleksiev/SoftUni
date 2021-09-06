from math import floor, ceil

x = int(input()) # кв.м лозето
y = float(input())   # гризде за един кв.м
z = int(input())  # нужни литри вино
workers = int(input())   # работници

total_grapes = x * y
wine = 0.40 * total_grapes / 2.5
difference_wine = abs(wine - z)

if wine < z:
    print(f"It will be a tough winter! More {floor(difference_wine)} liters wine needed.")
else:
    left_wine_for_workers = difference_wine / workers
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(difference_wine)} liters left -> {ceil(left_wine_for_workers)} liters per person.")
