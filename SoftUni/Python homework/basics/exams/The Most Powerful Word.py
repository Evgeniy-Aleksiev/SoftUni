import sys
from math import floor

command = input()

most_powerful_word = ""
max_points = -sys.maxsize
multiply = False

while command != "End of words":
    word = command
    points = 0
    count = 0
    for letter in word:
        count += 1
        let = ord(letter)
        points += let
        if count == 1 and (let == 65 or let == 97 or let == 69 or let == 101 or let == 73 or let == 105 or\
                           let == 79 or let == 111 or let == 85 or let == 117 or let == 89 or let == 121):
            multiply = True
    if multiply:
        points *= count
    else:
        points = floor(points / count)
    if points > max_points:
        max_points = points
        most_powerful_word = word
    command = input()

print(f"The most powerful word is {most_powerful_word} - {max_points}")