data = input().split()
occurrences = {}

for el in data:
    word = el.lower()
    if word not in occurrences:
        occurrences[word] = 0
    occurrences[word] += 1

[print(elements, end=" ") for (elements, quantity) in occurrences.items() if not quantity % 2 == 0]
