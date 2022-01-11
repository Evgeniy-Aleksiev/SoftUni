def calculates_total_price(products, quantity):
    if products == "coffee":
        return quantity * 1.5
    elif products == "water":
        return quantity
    elif products == "coke":
        return quantity * 1.40
    elif products == "snacks":
        return quantity * 2


order = input()
number_of_products = int(input())
total_price = calculates_total_price(order, number_of_products)
print(f"{total_price:.2f}")
