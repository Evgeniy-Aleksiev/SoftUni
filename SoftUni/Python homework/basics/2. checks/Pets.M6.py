from math import ceil

days = int(input())
food_kg = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_g = float(input())

turtle_food_per_day_g *= 0.001
sum = days * dog_food_per_day_kg + days * cat_food_per_day_kg + days * turtle_food_per_day_g

if sum <= food_kg:
    food_left = food_kg - sum
    print(f"{int(food_left)} kilos of food left.")
else:
    food_need = sum - food_kg
    print(f"{ceil(food_need)} more kilos of food are needed.")