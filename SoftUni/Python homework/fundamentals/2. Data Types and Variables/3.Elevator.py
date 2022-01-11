from math import ceil

people = int(input())
elevator_capacity = int(input())
result = ceil(people / elevator_capacity)
print(result)