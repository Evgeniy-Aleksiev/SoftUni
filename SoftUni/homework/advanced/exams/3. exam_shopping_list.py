def shopping_list(budget, **kwargs):
    bought_products = []

    if budget < 100:
        return 'You do not have enough budget.'

    for product, value in kwargs.items():
        price, quantity = value

        products_price = price * quantity

        if products_price <= budget:
            text = f'You bought {product} for {products_price:.2f} leva.'
            bought_products.append(text)
            budget -= products_price

        if len(bought_products) >= 5:
            break

    return '\n'.join(bought_products)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
