numbers = tuple(map(float, input().split()))
occurrences = {}

for num in numbers:
    if num not in occurrences:
        occurrences[num] = 0
    occurrences[num] += 1
[print(f"{number} - {count} times") for (number, count) in occurrences.items()]
