card = input().split(" ")

team_a = []
team_b = []
terminated = False

for current_card in card:
    if "A" in current_card:
        if current_card in team_a:
            continue
        else:
            team_a.append(current_card)
    elif "B" in current_card:
        if current_card in team_b:
            continue
        else:
            team_b.append(current_card)
    if len(team_a) == 5 or len(team_b) == 5:
        terminated = True
        break

players_team_a = 11 - len(team_a)
players_team_b = 11 - len(team_b)
print(f"Team A - {players_team_a}; Team B - {players_team_b}")
if terminated:
    print("Game was terminated")
