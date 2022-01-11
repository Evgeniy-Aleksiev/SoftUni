profit = float(input())
command = input()

reached_profit = False
club_income = 0

while command != "Party!":
    cocktail_name = command
    drinks_number = int(input())
    drink_price = 0
    discount_count = 0
    for letter in cocktail_name:
        drink_price += 1
    total_drink_price = drink_price * drinks_number
    if total_drink_price % 2 == 1 and discount_count < 1:
        total_drink_price *= 0.75
    club_income += total_drink_price
    if club_income >= profit:
        reached_profit = True
        break
    command = input()

if command == "Party!":
    money_need = profit - club_income
    print(f"We need {money_need:.2f} leva more.")
elif reached_profit:
    print("Target acquired.")
print(f"Club income - {club_income:.2f} leva.")

