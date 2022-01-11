import re

text = input()
pattern = r"(#|\|)([A-Za-z ]+)(\1)(\d{2}/\d{2}/\d{2})(\1)(\d+)(\1)"

days = 0
total_calories = 0
products = []

for match in re.finditer(pattern, text):
    total_calories += int(match.group(6))
    products.append([match.group(2), match.group(4), match.group(6)])

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for x in products:
    print(f"Item: {x[0]}, Best before: {x[1]}, Nutrition: {x[2]}")

