budget = float(input())
litters_fuel_need = float(input())
day_of_week = input()

fuel = litters_fuel_need * 2.10
total_price = fuel + 100
if day_of_week == "Saturday":
    total_price *= 0.90
elif day_of_week == "Sunday":
    total_price *= 0.80

difference = abs(budget - total_price)
if budget >= total_price:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")