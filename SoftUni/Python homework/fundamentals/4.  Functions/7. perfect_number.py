def sum_of_positive_int(number: int):
    proper_positive_divisors = []

    for current_number in range(1, number):
        if number % current_number == 0:
            proper_positive_divisors.append(current_number)

    return sum(proper_positive_divisors)


def is_perfect_number(number: int):
    if (sum_of_positive_int(number) + number) / 2 == number:
        perfect_number = True

        return perfect_number

    return False


def message(number: int):
    if is_perfect_number(number):
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number_input = int(input())
message(number_input)