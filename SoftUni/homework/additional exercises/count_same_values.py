def count_occurrences(values):
    occurrences = {}
    for num in values:
        if num not in occurrences:
            occurrences[num] = 0
        occurrences[num] += 1
    return occurrences


numbers = tuple(map(float, input().split()))
dictionary = count_occurrences(numbers)
[print(f"{number} - {count} times") for (number, count) in dictionary.items()]
