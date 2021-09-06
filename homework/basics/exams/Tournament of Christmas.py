number_tournaments = int(input())
total_money_earned = 0
total_wins = 0
total_loses = 0

for current_tournament in range(1, number_tournaments +1):
    command = input()
    wins = 0
    loses = 0
    money = 0
    while command != "Finish":
        result = input()
        if result == "win":
            wins += 1
            total_wins += 1
            money += 20
        elif result == "lose":
            loses += 1
            total_loses += 1
        command = input()
    if wins > loses:
        total_money_earned += money * 0.10 + money
    else:
        total_money_earned += money
if total_wins > total_loses:
    total_money_earned += total_money_earned * 0.20
    print(f"You won the tournament! Total raised money: {total_money_earned:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money_earned:.2f}")
