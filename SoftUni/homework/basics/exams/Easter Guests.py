from math import ceil

guest_number = int(input())
budget = int(input())

eastern_bread = ceil(guest_number / 3)
eastern_bread_price = eastern_bread * 4
eggs = guest_number * 2
eggs_price = eggs * 0.45
total_price = eggs_price + eastern_bread_price

difference = abs(total_price - budget)
if budget >= total_price:
    print(f"Lyubo bought {eastern_bread} Easter bread and {eggs} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")