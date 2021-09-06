budget = float(input())
command = input()

higher_than_budget = False
total_money = 0
product_count = 0

while command != "Stop":
    product_name = command
    product_price = float(input())
    product_count += 1
    if product_count % 3 == 0:
        product_price /= 2
    total_money += product_price
    if total_money > budget:
        higher_than_budget = True
        break
    command = input()

if command == "Stop":
    print(f"You bought {product_count} products for {total_money:.2f} leva.")
elif higher_than_budget:
    money_need = total_money - budget
    print("You don't have enough money!")
    print(f"You need {money_need:.2f} leva!")