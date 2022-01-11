budget = float(input())
category = input()
people_in_group = int(input())
price = 0
category_ticket = 0

if category == "VIP":
    category_ticket = people_in_group * 499.99
    if people_in_group <= 4:
        price = budget * 0.25
    elif people_in_group <= 9:
        price = budget * 0.40
    elif people_in_group <= 24:
        price = budget * 0.50
    elif people_in_group <= 49:
        price = budget * 0.60
    else:
        price = budget * 0.75

elif category == "Normal":
    category_ticket = people_in_group * 249.99
    if people_in_group <= 4:
        price = budget * 0.25
    elif people_in_group <= 9:
        price = budget * 0.40
    elif people_in_group <= 24:
        price = budget * 0.50
    elif people_in_group <= 49:
        price = budget * 0.60
    else:
        price = budget * 0.75

if category_ticket <= price:
    money_left = price - category_ticket
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_need = category_ticket - price
    print(f"Not enough money! You need {money_need:.2f} leva.")
