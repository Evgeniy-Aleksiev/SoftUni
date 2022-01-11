start_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())
combination = 0
found_combination = False

for first_number in range(start_of_interval, end_of_interval + 1):
    for second_number in range(start_of_interval, end_of_interval + 1):
        combination_sum = first_number + second_number
        combination += 1
        if combination_sum == magic_number:
            found_combination = True
            print(f"Combination N:{combination} ({first_number} + {second_number} = {magic_number})")
            break
    if found_combination:
        break
if not found_combination:
    print(f"{combination} combinations - neither equals {magic_number}")