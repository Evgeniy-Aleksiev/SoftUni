import sys

command = input()
winner_name = ""
max_points = -sys.maxsize
while command != "Stop":
    player_name = command
    points = 0
    for letter in player_name:
        let = ord(letter)
        number = int(input())
        if let == number:
            points += 10
        else:
            points += 2
    if points >= max_points:
        max_points = points
        winner_name = player_name
    command = input()

print(f"The winner is {winner_name} with {max_points} points!")