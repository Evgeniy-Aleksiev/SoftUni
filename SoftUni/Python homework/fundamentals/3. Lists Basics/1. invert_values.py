list_numbers = input().split(" ")

opposite_number = []

for current_number in list_numbers:
    number = int(current_number) * -1
    opposite_number.append(number)

print(opposite_number)