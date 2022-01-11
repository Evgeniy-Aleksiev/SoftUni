goal_to_reach = 10000
steps_taken = 0
going_home = False
while steps_taken < goal_to_reach:
    command = input()
    if command == "Going home":
        going_home = True
        steps_to_home = int(input())
        steps_taken += steps_to_home
        break
    steps = int(command)
    steps_taken += steps

difference = abs(steps_taken - goal_to_reach)
if steps_taken >= goal_to_reach:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")