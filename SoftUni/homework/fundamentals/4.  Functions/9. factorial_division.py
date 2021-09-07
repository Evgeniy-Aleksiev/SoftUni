def factorial_division(number_1: int, number_2: int):
    factorial_num_1 = 0
    factorial_num_2 = 0
    for current_number in range(number_1 - 1, 0, -1):
        if factorial_num_1 == 0:
            factorial_num_1 += number_1 * current_number
        else:
            factorial_num_1 = factorial_num_1 * current_number

    for current_number_2 in range(number_2 - 1, 0, - 1):
        if factorial_num_2 == 0:
            factorial_num_2 += number_2 * current_number_2
        else:
            factorial_num_2 = factorial_num_2 * current_number_2
    division = factorial_num_1 / factorial_num_2

    return division


num_1 = int(input())
num_2 = int(input())
print(f"{factorial_division(num_1, num_2):.2f}")