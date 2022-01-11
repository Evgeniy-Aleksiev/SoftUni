def stock_availability(products, command, *args):
    if command == 'delivery':
        return products + list(args)

    if not args or isinstance(args[0], int):
        products_cnt = args[0] if args else 1
        return products[products_cnt:]

    sold_items = set(args)

    return [item for item in products if item not in sold_items]


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "vanilla", "vanilla", "vanilla"))
