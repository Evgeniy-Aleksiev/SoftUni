budget = float(input())
nights = int(input())
price_per_night = float(input())
other_fees = int(input())
other_fees_price = other_fees / 100 * budget
if nights > 7:
    price_per_night *= 0.95
nights_price = nights * price_per_night
total_price = other_fees_price + nights_price

difference = abs(total_price - budget)
if total_price <= budget:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")