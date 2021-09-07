def first_factorial(number_1: int):
    factorial = 0
    for current_number in range(number_1 - 1, 0, - 1):
        if factorial == 0:
            factorial = number_1 * current_number
        else:
            factorial = factorial * current_number

    return factorial


def second_factorial(number_2: int):
    factorial = 0
    for current_number in range(number_2 - 1, 0, - 1):
        if factorial == 0:
            factorial = number_2 * current_number
        else:
            factorial = factorial * current_number

    return factorial


def division(number_1: int, number_2: int):
    factorial_division = first_factorial(number_1) / second_factorial(number_2)

    return factorial_division


num_1 = int(input())
num_2 = int(input())
print(f"{division(num_1, num_2):.2f}")
