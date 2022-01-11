from math import ceil

people = int(input())
fee_entry = float(input())
deck_chair_price = float(input())
umbrella_price = float(input())

total_entry_fee = people * fee_entry
total_umbrella = ceil(people * 0.50)
total_deck_chair = ceil(people * 0.75)
total_umbrella_price = total_umbrella * umbrella_price
total_deck_chair_price = total_deck_chair * deck_chair_price
total_price = total_umbrella_price + total_deck_chair_price + total_entry_fee
print(f"{total_price:.2f} lv.")