def characters_in_range(letter_1, letter_2):
    for current_characters in range(ord(letter_1) + 1, ord(letter_2)):
        print(chr(current_characters), end=" ")


let_1 = input()
let_2 = input()
characters_in_range(let_1, let_2)