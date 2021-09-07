elements = input().split()
bakery = {}

for index in range(0, len(elements), 2):
    product = elements[index]
    quantity = int(elements[index + 1])
    bakery[product] = quantity

searched_product = input().split()
for current_product in searched_product:
    if current_product in bakery:
        print(f"We have {bakery[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")
