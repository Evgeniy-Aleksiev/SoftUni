days = int(input())
total_food = float(input())

biscuits = 0
total_eaten_food = 0
food_eaten_by_dog = 0
food_eaten_by_cat = 0
for per_day in range(1, days +1):
    dogs_food = int(input())
    cats_food = int(input())
    total_eaten_food += dogs_food + cats_food
    food_eaten_by_dog += dogs_food
    food_eaten_by_cat += cats_food
    if per_day % 3 == 0 and per_day > 1:
        biscuits += (dogs_food + cats_food) * 0.10

print(f"Total eaten biscuits: {round(biscuits)}gr.")
total_food_percent = total_eaten_food / total_food * 100
print(f"{total_food_percent:.2f}% of the food has been eaten.")
food_eaten_by_dog_percent = food_eaten_by_dog / total_eaten_food * 100
print(f"{food_eaten_by_dog_percent:.2f}% eaten from the dog.")
food_eaten_by_cat_percent = food_eaten_by_cat / total_eaten_food * 100
print(f"{food_eaten_by_cat_percent:.2f}% eaten from the cat.")