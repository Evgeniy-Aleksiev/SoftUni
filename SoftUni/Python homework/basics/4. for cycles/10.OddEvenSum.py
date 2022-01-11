n = int(input())
sum_even = 0
sum_odd = 0
difference = 0

for x in range(1, n + 1):
    number = int(input())
    if x % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

if sum_even == sum_odd:
    print("Yes")
    print(f"Sum = {sum_odd}")
else:
    difference = abs(sum_even - sum_odd)
    print("No")
    print(f"Diff = {difference}")
