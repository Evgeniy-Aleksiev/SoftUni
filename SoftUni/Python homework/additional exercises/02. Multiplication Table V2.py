first_number = 1
second_number = 1

while first_number < 11:
    while second_number < 11:
        result = first_number * second_number
        print(f"{first_number} * {second_number} = {result}")
        second_number += 1
    first_number += 1
    second_number = 1
