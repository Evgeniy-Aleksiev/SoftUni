n, headers, total = int(input()), list(input().split()), 0
for x in range(n):
    total += int(list(input().split())[headers.index('MARKS')])
print(f"{total/n:.2f}")
