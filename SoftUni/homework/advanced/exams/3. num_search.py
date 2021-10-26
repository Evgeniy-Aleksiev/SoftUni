def numbers_searching(*args):
    sequence_numbers = list(args)
    result = []
    duplicates = []
    min_num = min(sequence_numbers)
    max_num = max(sequence_numbers)

    for number in range(min_num, max_num + 1):
        if number not in sequence_numbers:
            result.append(number)
            continue
        duplicate_num = sequence_numbers.count(number)
        if duplicate_num > 1:
            duplicates.append(number)
    result.append(duplicates)
    return result

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
