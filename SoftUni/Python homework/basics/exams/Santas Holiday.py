days = int(input())
room = input()
evaluation = input()
nights = days - 1

price_per_night = 0
if room == "room for one person":
    price_per_night += 18 * nights
elif room == "apartment":
    price_per_night += 25 * nights
    if days < 10:
        price_per_night *= 0.70
    elif days < 15:
        price_per_night *= 0.65
    else:
        price_per_night *= 0.50
elif room == "president apartment":
    price_per_night += 35 * nights
    if days < 10:
        price_per_night *= 0.90
    elif days < 15:
        price_per_night *= 0.85
    else:
        price_per_night *= 0.80

if evaluation == "positive":
    price_per_night += price_per_night * 0.25
elif evaluation == "negative":
    price_per_night *= 0.90

print(f"{price_per_night:.2f}")