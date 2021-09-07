goal_to_reach = 10000
total_steps = 0
goal_reached = False
command = input()

while command != "Going home":
    steps = int(command)
    total_steps += steps
    if total_steps >= goal_to_reach:
        goal_reached = True
        break
    else:
        command = input()

if command == "Going home":
    steps_to_home = int(input())
    total_steps += steps_to_home

difference = abs(total_steps - goal_to_reach)
if total_steps >= goal_to_reach:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")