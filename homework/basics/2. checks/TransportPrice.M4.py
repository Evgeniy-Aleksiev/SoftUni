n = int(input())
day_night = input()
price = 0
if n < 20:
    if day_night == "day":
        price += 0.70 + (n * 0.79)
    elif day_night == "night":
        price += 0.70 + (n * 0.90)
elif n < 100:
    price += n * 0.09
else:
    price += n * 0.06

print(f"{price:.2f}")