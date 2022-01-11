from math import ceil

n = int(input())

stars = 1
if n % 2 == 0:
    stars += 1

roof_length = ceil(n / 2)

for roof in range(roof_length):
    padding = (n - stars) // 2
    line = '-' * padding + '*' * stars + '-' * padding
    print(line)
    stars += 2
for basis in range(n // 2):
    line = '|' + '*' * (n - 2) + '|'
    print(line)