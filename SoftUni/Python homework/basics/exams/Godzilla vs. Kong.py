movie_budget = float(input())
statists = int(input())
price_for_clothes_per_statist = float(input())

decor = movie_budget * 0.10
cloths_price = statists * price_for_clothes_per_statist
if statists >= 150:
    cloths_price *= 0.90
movie_price = decor + cloths_price
total_movie_price = abs(movie_budget - movie_price)

if movie_budget >= movie_price:
    print("Action!")
    print(f"Wingard starts filming with {total_movie_price:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_movie_price:.2f} leva more.")