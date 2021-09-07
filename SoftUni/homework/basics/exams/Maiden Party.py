maiden_party_price = float(input())
love_message_number = int(input())
roses_number = int(input())
keychain_number = int(input())
cartoons_number = int(input())
good_luck_surprise_number = int(input())

total_price = love_message_number * 0.60 + roses_number * 7.20 + keychain_number * 3.60 +\
    cartoons_number * 18.20 + good_luck_surprise_number * 22
total_number = love_message_number + roses_number + keychain_number + cartoons_number + good_luck_surprise_number

if total_number >= 25:
    total_price *= 0.65
hosting_costs = total_price * 0.90

difference = abs(hosting_costs - maiden_party_price)
if hosting_costs >= maiden_party_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")