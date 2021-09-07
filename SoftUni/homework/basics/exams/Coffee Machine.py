drink = input()
sugar = input()
number_drinks = int(input())

price = 0
if drink == "Espresso":
    if sugar == "Without":
        price += 0.90 * number_drinks
    elif sugar == "Normal":
        price += 1 * number_drinks
    elif sugar == "Extra":
        price += 1.20 * number_drinks
elif drink == "Cappuccino":
    if sugar == "Without":
        price += 1 * number_drinks
    elif sugar == "Normal":
        price += 1.20 * number_drinks
    elif sugar == "Extra":
        price += 1.60 * number_drinks
elif drink == "Tea":
    if sugar == "Without":
        price += 0.50 * number_drinks
    elif sugar == "Normal":
        price += 0.60 * number_drinks
    elif sugar == "Extra":
        price += 0.70 * number_drinks

if sugar == "Without":
    price *= 0.65
if drink == "Espresso" and number_drinks >= 5:
    price *= 0.75
if price > 15:
    price *= 0.80

print(f"You bought {number_drinks} cups of {drink} for {price:.2f} lv.")