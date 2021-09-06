kind_of_flower = input()   # Roses, Dahlias, Tulips, Narcissus, Gladiolus
number_flowers = int(input())
budget = int(input())
price = 0

if kind_of_flower == "Roses":
    price = number_flowers * 5
    if number_flowers > 80:
        price *= 0.90
elif kind_of_flower == "Dahlias":
    price = number_flowers * 3.80
    if number_flowers > 90:
        price *= 0.85
elif kind_of_flower == "Tulips":
    price = number_flowers * 2.80
    if number_flowers > 80:
        price *= 0.85
elif kind_of_flower == "Narcissus":
    price = number_flowers * 3
    if number_flowers < 120:
        price += price * 0.15
elif kind_of_flower == "Gladiolus":
    price = number_flowers * 2.50
    if number_flowers < 80:
        price += price * 0.20

if price <= budget:
    money_left = budget - price
    print(f"Hey, you have a great garden with {number_flowers} {kind_of_flower} and {money_left:.2f} leva left.")
else:
    money_need = price - budget
    print(f"Not enough money, you need {money_need:.2f} leva more.")