number = int(input())
sum = 0

for count in range(number):
    count = int(input())
    sum += count
average_number = sum / number
print(f"{average_number:.2f}")