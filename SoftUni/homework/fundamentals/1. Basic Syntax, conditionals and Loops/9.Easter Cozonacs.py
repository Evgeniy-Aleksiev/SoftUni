budget = float(input())
flour_kg_price = float(input())
cozonacs_count = 0
colored_eggs = 0
eggs_price = flour_kg_price * 0.75
milk_price = flour_kg_price * 1.25 / 4
cozonac_price = eggs_price + milk_price + flour_kg_price

while cozonac_price < budget:
    budget -= cozonac_price
    cozonacs_count += 1
    colored_eggs += 3
    if cozonacs_count % 3 == 0:
        colored_eggs -= cozonacs_count - 2
print(f"You made {cozonacs_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")