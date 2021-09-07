import sys

command = input()
player_name = " "
max_goals = -sys.maxsize

while command != "END":
    player = command
    player_goals = int(input())
    if player_goals > max_goals:
        max_goals = player_goals
        player_name = player
    if player_goals >= 10:
        break

    command = input()

print(f"{player_name} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")