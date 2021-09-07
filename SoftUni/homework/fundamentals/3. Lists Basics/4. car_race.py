number = input().split()

half = len(number) // 2
left_car = number[:half]
right_car = number[:half:-1]

left_racer_sum = 0
right_racer_sum = 0


for x in left_car:
    if int(x) == 0:
        left_racer_sum *= 0.8
    else:
        left_racer_sum += int(x)

for i in right_car:
    if int(i) == 0:
        right_racer_sum *= 0.8
    else:
        right_racer_sum += int(i)

if left_racer_sum < right_racer_sum:
    print(f"The winner is left with total time: {left_racer_sum:.1f}")
elif right_racer_sum < left_racer_sum:
    print(f"The winner is right with total time: {right_racer_sum:.1f}")
