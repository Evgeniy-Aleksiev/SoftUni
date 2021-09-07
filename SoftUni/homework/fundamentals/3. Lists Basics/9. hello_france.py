items_with_their_price = input().split("|")
budget = float(input())

bought_items_price = []
sold_items_profit = []

for current_item in items_with_their_price:
    item_split = current_item.split("->")
    item_type = item_split[0]
    item_price = float(item_split[1])

    if item_type == "Clothes":
        if item_price <= 50 and item_price <= budget:
            budget -= item_price
            profit = item_price * 0.40 + item_price
            bought_items_price.append(item_price)
            sold_items_profit.append(profit)

    elif item_type == "Shoes":
        if item_price <= 35 and item_price <= budget:
            budget -= item_price
            profit = item_price * 0.40 + item_price
            bought_items_price.append(item_price)
            sold_items_profit.append(profit)

    elif item_type == "Accessories":
        if item_price <= 20.50 and item_price <= budget:
            budget -= item_price
            profit = item_price * 0.40 + item_price
            bought_items_price.append(item_price)
            sold_items_profit.append(profit)

total_profit = sum(sold_items_profit) - sum(bought_items_price)

for items_profit in sold_items_profit:
    print(f"{items_profit:.2f}", end=" ")
print()

print(f"Profit: {total_profit:.2f}")
sum_of_new_prices = sum(sold_items_profit) + budget

if sum_of_new_prices >= 150:
    print("Hello, France!")
else:
    print("Time to go.")