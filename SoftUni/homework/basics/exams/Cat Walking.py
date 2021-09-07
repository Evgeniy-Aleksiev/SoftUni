walk_minutes = int(input())
walk_number_per_day = int(input())
calories = int(input())

total_minutes = walk_minutes * walk_number_per_day
total_calories_burn = total_minutes * 5
enough_calories_burn = calories * 0.50

if total_calories_burn >= enough_calories_burn:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burn}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories_burn}.")