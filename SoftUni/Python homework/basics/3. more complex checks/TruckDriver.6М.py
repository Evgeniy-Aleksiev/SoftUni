season = input()
monthly_km = float(input())
distance = 0
salary = 0

if monthly_km <= 5000:
    if season == "Spring" or season == "Autumn":
        distance = monthly_km * 0.75
    elif season == "Summer":
        distance = monthly_km * 0.90
    elif season == "Winter":
        distance = monthly_km * 1.05
elif monthly_km <= 10000:
    if season == "Spring" or season == "Autumn":
        distance = monthly_km * 0.95
    elif season == "Summer":
        distance = monthly_km * 1.10
    elif season == "Winter":
        distance = monthly_km * 1.25
elif monthly_km <= 20000:
    distance = monthly_km * 1.45

price = (distance * 4) * 0.90
print(f"{price:.2f}")