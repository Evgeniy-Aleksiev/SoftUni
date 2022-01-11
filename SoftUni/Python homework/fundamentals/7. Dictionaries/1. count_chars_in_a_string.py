word = input().split()
chars_count = {}

for element in word:
    for index in range(len(element)):
        letter = element[index]
        if letter not in chars_count:
            chars_count[letter] = 1
        else:
            chars_count[letter] += 1

for key, value in chars_count.items():
    print(f"{key} -> {value}")

