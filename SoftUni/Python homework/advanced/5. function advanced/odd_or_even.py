command = input()
numbers = [int(x) for x in input().split()]

com = 1 if command == "Odd" else 0
total_sum = sum(filter(lambda x: x % 2 == com, numbers))
print(total_sum * len(numbers))