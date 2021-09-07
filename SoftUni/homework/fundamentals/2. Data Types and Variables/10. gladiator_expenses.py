lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
shield_break = 0

for current_lost in range(1, lost_fights_count + 1):
    if current_lost % 2 == 0:
        expenses += helmet_price
    if current_lost % 3 == 0:
        expenses += sword_price
    if current_lost % 2 == 0 and current_lost % 3 == 0:
        expenses += shield_price
        shield_break += 1
    if shield_break == 2:
        expenses += armor_price
        shield_break = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")