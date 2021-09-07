money_in_hand = float(input())
gender = input()
age = int(input())
sport = input()

price_subscription = 0
if gender == "m":
    if sport == "Gym":
        price_subscription += 42
    elif sport == "Boxing":
        price_subscription += 41
    elif sport == "Yoga":
        price_subscription += 45
    elif sport == "Zumba":
        price_subscription += 34
    elif sport == "Dances":
        price_subscription += 51
    elif sport == "Pilates":
        price_subscription += 39
elif gender == "f":
    if sport == "Gym":
        price_subscription += 35
    elif sport == "Boxing":
        price_subscription += 37
    elif sport == "Yoga":
        price_subscription += 42
    elif sport == "Zumba":
        price_subscription += 31
    elif sport == "Dances":
        price_subscription += 53
    elif sport == "Pilates":
        price_subscription += 37

if age <= 19:
    price_subscription *= 0.80

if money_in_hand >= price_subscription:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    money_need = price_subscription - money_in_hand
    print(f"You don't have enough money! You need ${money_need:.2f} more.")