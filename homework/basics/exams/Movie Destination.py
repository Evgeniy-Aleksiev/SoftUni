budget = float(input())
destination = input()
season = input()
days = int(input())

total_price = 0
price_per_day = 0
if destination == "Dubai":
    if season == "Winter":
        price_per_day = 45000
    elif season == "Summer":
        price_per_day = 40000
    total_price = (price_per_day * days) * 0.70

elif destination == "Sofia":
    if season == "Winter":
        price_per_day = 17000
    elif season == "Summer":
        price_per_day = 12500
    price = price_per_day * days
    total_price = price * 0.25 + price
elif destination == "London":
    if season == "Winter":
        price_per_day = 24000
    elif season == "Summer":
        price_per_day = 20250
    total_price = price_per_day * days

difference = abs(budget - total_price)
if budget >= total_price:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")