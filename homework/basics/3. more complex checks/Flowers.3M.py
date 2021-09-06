chrysanthemums = int(input()) # Хризантеми
roses = int(input())
tulips = int(input())
seasons = input()
holiday = input()
price = 0
total_flowers = chrysanthemums + roses + tulips

if seasons == "Spring" or seasons == "Summer":
    chrysanthemums_price = chrysanthemums * 2
    roses_price = roses * 4.10
    tulips_price = tulips * 2.50
    price = chrysanthemums_price + roses_price + tulips_price
    if holiday == "Y":
        price = price * 0.15 + price
    if seasons == "Spring" and tulips > 7:
        price *= 0.95

elif seasons == "Autumn" or seasons == "Winter":
    chrysanthemums_price = chrysanthemums * 3.75
    roses_price = roses * 4.50
    tulips_price = tulips * 4.15
    price = chrysanthemums_price + roses_price + tulips_price
    if holiday == "Y":
        price = price * 0.15 + price
    if seasons == "Winter" and roses >= 10:
        price *= 0.90

if total_flowers > 20:
    price *= 0.80

total_price = price + 2
print(f"{total_price:.2f}")