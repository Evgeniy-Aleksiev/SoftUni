periodic_table = set()

for _ in range(int(input())):
    current_element = set(input().split())
    periodic_table = periodic_table.union(current_element)

[print(x) for x in periodic_table]
