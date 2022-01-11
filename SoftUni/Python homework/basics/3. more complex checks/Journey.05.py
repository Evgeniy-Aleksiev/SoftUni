budget = float(input())
season = input()
price = 0
destination = " "
camp_or_hotel = " "

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        camp_or_hotel = "Camp"
        price = budget * 0.70
    elif season == "winter":
        camp_or_hotel = "Hotel"
        price = budget * 0.30
elif budget > 1000:
    destination = "Europe"
    camp_or_hotel = "Hotel"
    price = budget * 0.10
else:
    destination = "Balkans"
    if season == "summer":
        camp_or_hotel = "Camp"
        price = budget * 0.60
    elif season == "winter":
        camp_or_hotel = "Hotel"
        price = budget * 0.20

print(f"Somewhere in {destination}" )
print(f"{camp_or_hotel} - {budget - price:.2f}")