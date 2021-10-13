from math import log

first_number = int(input())
base = input()

if base == 'natural':
    print(f"{log(first_number):.2f}")
else:
    print(f"{log(first_number, int(base)):.2f}")
