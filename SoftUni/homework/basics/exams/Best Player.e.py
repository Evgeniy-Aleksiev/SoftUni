import sys

command = input()
max_goals = -sys.maxsize
player = ' '

while command != "END":
    player_name = command
    goal_number = int(input())
    if goal_number > max_goals:
        max_goals = goal_number
        player = player_name
    if goal_number >= 10:
        break
    command = input()
print(f"{player} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")