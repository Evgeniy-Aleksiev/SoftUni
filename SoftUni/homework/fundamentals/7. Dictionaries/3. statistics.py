data = input()
bakery = {}

while not data == "statistics":
    food, quantity = data.split(": ")
    if food not in bakery:
        bakery[food] = 0
    bakery[food] += int(quantity)

    data = input()

print("Products in stock:")
[print(f"- {product}: {quantity}") for (product, quantity) in bakery.items()]
print(f"Total Products: {len(bakery)}")
print(f"Total Quantity: {sum(bakery.values())}")