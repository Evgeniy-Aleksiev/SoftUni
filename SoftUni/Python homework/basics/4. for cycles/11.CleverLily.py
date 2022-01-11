age = int(input())
price_washing_machine = float(input())
toy_price = int(input())

toys = 0
price_earned = 0
saved_money = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 1:
        toys += 1
    else:
        price_earned += birthday * 5 - 1

saved_money = price_earned + (toy_price * toys)
if saved_money >= price_washing_machine:
    money_left = saved_money - price_washing_machine
    print(f"Yes! {money_left:.2f}")
else:
    money_need = price_washing_machine - saved_money
    print(f"No! {money_need:.2f}")

