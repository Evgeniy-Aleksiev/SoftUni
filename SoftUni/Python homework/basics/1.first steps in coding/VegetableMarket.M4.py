vegetable_price = float(input())
fruit_price = float(input())
quantity_vegetable = int(input())
quantity_fruit = int(input())

sum = vegetable_price * quantity_vegetable + fruit_price * quantity_fruit
final_sum = sum / 1.94
print("{:.2f}".format(final_sum))