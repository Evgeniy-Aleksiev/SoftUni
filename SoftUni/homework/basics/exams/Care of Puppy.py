food = int(input())
command = input()

kg_to_gram_food = food * 1000
total_eaten_food = 0

while command != "Adopted":
    eaten_food = int(command)
    total_eaten_food += eaten_food
    command = input()

if kg_to_gram_food >= total_eaten_food:
    print(f"Food is enough! Leftovers: {kg_to_gram_food - total_eaten_food} grams.")
else:
    print(f"Food is not enough. You need {total_eaten_food - kg_to_gram_food} grams more.")