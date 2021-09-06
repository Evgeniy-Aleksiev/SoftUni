number = int(input())
combinations_count = 0

for first_number in range(number + 1):
    for second_number in range(number + 1):
        for third_number in range(number + 1):
            if first_number + second_number + third_number == number:
                combinations_count += 1
print(combinations_count)