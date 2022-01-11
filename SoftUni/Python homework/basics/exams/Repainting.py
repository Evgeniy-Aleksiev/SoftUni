nylon_amount = int(input())
paint_amount = int(input())
thinner_amount = int(input())
hours_need = int(input())

nylon_price = (nylon_amount + 2) * 1.50
paint_price = (paint_amount * 0.10 + paint_amount) * 14.50
thinner_price = thinner_amount * 5
price_sum = nylon_price + paint_price + thinner_price + 0.40
total_price = (price_sum * 0.30 * hours_need) + price_sum
print(f"Total expenses: {total_price:.2f} lv.")