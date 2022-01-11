minutes = int(input())
seconds = int(input())
chute_length = float(input())
seconds_for_100m = int(input())

seconds_control = minutes * 60 + seconds
decrease = chute_length / 120
time_decrease = chute_length / 120 * 2.5
time = ((chute_length / 100) * seconds_for_100m) - time_decrease

if time <= seconds_control:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    not_enough = time - seconds_control
    print(f"No, Marin failed! He was {not_enough:.3f} second slower.")

