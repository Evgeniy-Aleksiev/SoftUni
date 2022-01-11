from math import ceil

serial_name = input()
episode_time = int(input())
rest_time = int(input())

lunch_time = rest_time / 8
relax_time = rest_time / 4
time_left = rest_time - lunch_time - relax_time

difference = abs(time_left - episode_time)
if episode_time <= time_left:
    print(f"You have enough time to watch {serial_name} and left with {ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(difference)} more minutes.")