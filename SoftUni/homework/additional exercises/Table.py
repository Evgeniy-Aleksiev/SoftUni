first_number = 1
second_number = 1
third_number = 1

while first_number < 11:
    while second_number < 11:
        while third_number < 11:
            result = first_number * second_number * third_number
            print(f"{first_number} * {second_number} * {third_number} = {result}", end=", ")
            third_number += 1
        print()
        second_number += 1
        third_number = 1
    print()
    first_number += 1
    second_number = 1
    third_number = 0