stadium_capacity = int(input())
fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0
for sector in range(fans):
    sector = input()
    if sector == "A":
        fans_a += 1
    elif sector == "B":
        fans_b += 1
    elif sector == "V":
        fans_v += 1
    elif sector == "G":
        fans_g += 1

total_fans = fans / stadium_capacity * 100
print(f"{(fans_a / fans * 100):.2f}%")
print(f"{(fans_b / fans * 100):.2f}%")
print(f"{(fans_v / fans * 100):.2f}%")
print(f"{(fans_g / fans * 100):.2f}%")
print(f"{total_fans:.2f}%")