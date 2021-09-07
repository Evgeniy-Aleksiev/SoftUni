data = input()

product = {}

while not data == "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)
    if name not in product:
        product[name] = {f"price": price, "quantity": quantity}
    else:
        product[name]['price'] = price
        product[name]['quantity'] += quantity
    data = input()

for key, value in product.items():
    price = value['price'] * value['quantity']
    print(f"{key} -> {price:.2f}")
