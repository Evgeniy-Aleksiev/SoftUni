letter = input().split()

first_position = 0
last_position = 0
total_sum = 0
i = 1

for el in letter:
    while not first_position > 0 or not last_position > 0:
        first_letter = 64 + i
        last_letter = 64 + i
        if not first_position == 0 and not last_position == 0:
            break
        if chr(first_letter) == el[0].upper():
            first_position = i
        if chr(last_letter) == el[-1].upper():
            last_position = i
        i += 1

    number = int(el[1:-1])
    result_number = 0
    if el[0].isupper():
        result_number += number / first_position
    else:
        result_number += number * first_position
    if el[-1].isupper():
        total_sum += result_number - last_position
    else:
        total_sum += result_number + last_position

    first_position = 0
    last_position = 0
    i = 0

print(f"{total_sum:.2f}")
