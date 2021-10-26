def numbers_searching(*args):
    duplicate_numbers = []
    missing_number = []
    numbers = sorted(args)
    numbers_set = set(args)
    min_num = min(numbers_set)
    max_num = max(numbers_set)

    for num in numbers_set:
        x = numbers.count(num)
        if x > 1:
            duplicate_numbers.append(num)

    for num in range(min_num, max_num + 1):
        if num not in numbers_set:
            missing_number.append(num)
            break
    missing_number.append(duplicate_numbers)

    return missing_number


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
