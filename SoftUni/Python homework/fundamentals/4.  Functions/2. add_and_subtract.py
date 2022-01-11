def sum_of_numbers(number_1: int, number_2: int):
    total = number_1 + number_2

    return total


def subtract_numbers(sum_1: int, number_3: int):
    return sum_1 - number_3


def add_and_subtract(number_1: int, number_2: int, number_3: int):
    sum_1 = sum_of_numbers(number_1, number_2)
    result = subtract_numbers(sum_1, number_3)

    return result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(add_and_subtract(num_1, num_2, num_3))