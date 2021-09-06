n = int(input())
left_sum = 0
right_sum = 0
difference = 0

for left_number in range(1, n +1):
    left_number = int(input())
    left_sum += left_number

for right_number in range(1, n +1):
    right_number = int(input())
    right_sum += right_number

if left_sum == right_sum:
    print(f" Yes, sum = {left_sum} " )
else:
    difference = abs(left_sum - right_sum)
    print(f" No, diff = {difference}")