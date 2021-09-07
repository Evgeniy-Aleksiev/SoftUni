import re

pattern = r">>(?P<furniture_name>[A-Za-z]+)<<(?P<price>\d+\.*\d+)!(?P<quantity>\d+)"
furniture = []
total_price = 0
text = input()

while not text == "Purchase":
    matched = re.match(pattern, text)

    if matched is not None:
        furniture.append(matched.group("furniture_name"))
        total_price += float(matched.group("price")) * int(matched.group("quantity"))

    text = input()

print("Bought furniture:")
[print(product) for product in furniture]
print(f"Total money spend: {total_price:.2f}")
