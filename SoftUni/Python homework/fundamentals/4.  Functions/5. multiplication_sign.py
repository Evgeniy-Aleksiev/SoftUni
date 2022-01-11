def get_result(num1, num2, num3):
    list_of_numbers = [num1, num2, num3]

    negative_numbers_count = 0

    for current_number in list_of_numbers:
        if current_number < 0:
            negative_numbers_count += 1

    if 0 in list_of_numbers:
        print("zero")

    elif not negative_numbers_count % 2 == 0:
        print("negative")

    else:
        print("positive")


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
get_result(number_1, number_2, number_3)