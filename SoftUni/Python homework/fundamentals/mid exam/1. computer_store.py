data = input()

total_price = 0

while not data == "special" and not data == "regular":
    price = float(data)
    if price < 0:
        print("Invalid price!")
    else:
        total_price += price

    data = input()
taxes = total_price * 0.20
total_price_with_taxes = taxes + total_price
if data == "special":
    total_price_with_taxes = total_price_with_taxes - (total_price_with_taxes * 0.10)

if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price_with_taxes:.2f}$")
