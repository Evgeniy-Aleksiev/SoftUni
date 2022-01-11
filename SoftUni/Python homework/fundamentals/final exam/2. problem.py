import re

n = int(input())
pattern = r"\!([A-Z][a-z]{2,})\!\:\[([A-Za-z]{8,})\]"

for _ in range(n):
    word = input()
    invalid = True

    element = re.finditer(pattern, word)
    list_of_numbers = []

    for el in element:
        for char in el.group(2):
            list_of_numbers.append(str(ord(char)))
        print(f"{el.group(1)}: {' '.join(list_of_numbers)}")
        invalid = False

    if invalid:
        print("The message is invalid")