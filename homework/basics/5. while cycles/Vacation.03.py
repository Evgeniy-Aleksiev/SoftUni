vacation_money = float(input())
money_in_hand = float(input())
spending_days = 0
days_count = 0

while vacation_money > money_in_hand and spending_days < 5:
    command = input()
    money = float(input())
    days_count += 1
    if command == "save":
        money_in_hand += money
        spending_days = 0
    else:
        money_in_hand -= money
        spending_days += 1
        if money_in_hand < 0:
            money_in_hand = 0
if spending_days == 5:
    print("You can't save the money.")
    print(days_count)
if vacation_money <= money_in_hand:
    print(f"You saved the money for {days_count} days.")