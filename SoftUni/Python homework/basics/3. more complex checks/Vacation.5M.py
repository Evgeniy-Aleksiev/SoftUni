budget = float(input())
season = input()
accommodation = " "
place = " "
price = 0

if season == "Summer":
    place = "Alaska"
    if budget <= 1000:
        accommodation = "Camp"
        price = budget * 0.65
    elif budget <= 3000:
        accommodation = "Hut"
        price = budget * 0.80
    else:
        accommodation = "Hotel"
        price = budget * 0.90
elif season == "Winter":
    place = "Morocco"
    if budget <= 1000:
        accommodation = "Camp"
        price = budget * 0.45
    elif budget <= 3000:
        accommodation = "Hut"
        price = budget * 0.60
    else:
        accommodation = "Hotel"
        price = budget * 0.90
        
print(f"{place} - {accommodation} - {price:.2f}")