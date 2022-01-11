budget = int(input())
season = input()
number_fishers = int(input())
price = 0

if season == "Spring":
    if number_fishers <= 6:
        price = 3000 * 0.90
    elif number_fishers >= 12:
        price = 3000 * 0.75
    else:
        price = 3000 * 0.85
elif season == "Summer" or season == "Autumn":
    if number_fishers <= 6:
        price = 4200 * 0.90
    elif number_fishers >= 12:
        price = 4200 * 0.75
    else:
        price = 4200 * 0.85
elif season == "Winter":
    if number_fishers <= 6:
        price = 2600 * 0.90
    elif number_fishers >= 12:
        price = 2600 * 0.75
    else:
        price = 2600 * 0.85

if season == "Spring" or season == "Summer" or season == "Winter":
    if number_fishers % 2 == 0:
        price *= 0.95

if budget >= price:
    money_left = budget - price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_need = price - budget
    print(f"Not enough money! You need {money_need:.2f} leva.")
