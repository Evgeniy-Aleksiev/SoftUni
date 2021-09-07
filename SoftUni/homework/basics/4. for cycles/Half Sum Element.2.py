import sys

n = int(input())
max = -sys.maxsize
sum = 0

for number in range(n):
    number = int(input())
    if number > max:
        max = number

    sum += number

if max == sum - max:
    print("Yes")
    print(f"Sum = {max}")
else:
    difference = sum - max
    print("No")
    print(f"Diff = {abs(difference - max)}")
