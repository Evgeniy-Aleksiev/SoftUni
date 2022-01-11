number = int(input())

for current_number in range(1, number + 1):
    sum_of_digits = 0
    digit = str(current_number)
    for current_digit in digit:
        sum_of_digits += int(current_digit)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{current_number} -> True")
    else:
        print(f"{current_number} -> False")