command = input()
numbers = [int(x) for x in input().split()]
current_sum = 0

com = 1 if command == 'Odd' else 0

for num in numbers:
    if num % 2 == com:
        current_sum += num

print(current_sum * len(numbers))