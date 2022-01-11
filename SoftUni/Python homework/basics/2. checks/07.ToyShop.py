price_trip = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

total_toys = puzzles + dolls + teddy_bears + minions + trucks
total_price = puzzles * 2.60 + dolls * 3 + teddy_bears * 4.10 + minions * 8.20 + trucks * 2

if total_toys >= 50:
    discount = total_price * 0.25
    total_price = total_price - discount

rent = total_price * 0.10
profit = total_price - rent

if profit >= price_trip:
    left_money = profit - price_trip
    print(f"Yes! {left_money:.2f} lv left.")
else:
    need_money = price_trip - profit
    print(f"Not enough money! {need_money:.2f} lv needed.")