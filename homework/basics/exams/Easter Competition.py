import sys

eastern_bread_number = int(input())
max_evaluation = -sys.maxsize
top_chief = " "
chief = " "

for eastern_bread in range(eastern_bread_number):
    chief = input()
    command = input()
    points = 0
    while command != "Stop":
        evaluation = int(command)
        points += evaluation
        command = input()
    print(f"{chief} has {points} points.")
    if points > max_evaluation:
        max_evaluation = points
        top_chief = chief
        print(f"{chief} is the new number 1!")

print(f"{top_chief} won competition with {max_evaluation} points!")
