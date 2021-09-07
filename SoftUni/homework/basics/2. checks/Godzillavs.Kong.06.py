budget = float(input())
number_statist = int(input())
price_clothes_statist1 = float(input())

decor = budget * 0.10
clothes = number_statist * price_clothes_statist1

if number_statist > 150:
    clothes = clothes - (clothes * 0.10)

sum = clothes + decor
movie_price =abs(budget - (clothes + decor))
if sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {movie_price:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {movie_price:.2f} leva left.")